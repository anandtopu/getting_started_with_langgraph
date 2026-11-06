"""Authenticated streaming claims API. Local tests use in-process HTTP without a socket."""

import hmac
import re
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field, StrictBool

from common.copilot.v10 import AuthorizedContext
from common.data import load_submission
from common.service import BusyThread, Principal
from common.sse import encode_event


class CreateThread(BaseModel):
    thread_id: str = Field(pattern=r"^[a-zA-Z0-9_-]{1,80}$")
    submission: int = Field(ge=1, le=60)


class ResumeThread(BaseModel):
    interrupt_id: str
    approved: StrictBool | None = None
    coverage_confirmed: StrictBool = False
    document_id: str | None = None
    received_on: str | None = None


def create_app(
    graph=None, registry=None, tokens: dict[str, Principal] | None = None, resource_factory=None
):
    @asynccontextmanager
    async def lifespan(app):
        if resource_factory:
            async with resource_factory() as resources:
                app.state.graph, app.state.registry = resources
                yield
        else:
            yield

    app = FastAPI(title="Larkspur synthetic claims", lifespan=lifespan)
    app.state.graph, app.state.registry = graph, registry
    token_map = dict(tokens or {})
    if not token_map or any(len(token) < 16 for token in token_map):
        raise ValueError("Configure API tokens of at least 16 characters")

    def authenticate(authorization: Annotated[str | None, Header()] = None) -> Principal:
        supplied = (
            authorization.removeprefix("Bearer ")
            if authorization and authorization.startswith("Bearer ")
            else ""
        )
        for token, principal in token_map.items():
            if hmac.compare_digest(supplied, token):
                return principal
        raise HTTPException(401, "Authentication required")

    identity = Annotated[Principal, Depends(authenticate)]

    async def ownership(thread_id: str, principal: Principal):
        if not re.fullmatch(r"[a-zA-Z0-9_-]{1,80}", thread_id):
            raise HTTPException(404, "Thread unavailable")
        try:
            return await app.state.registry.claim(thread_id, principal)
        except PermissionError:
            raise HTTPException(404, "Thread unavailable") from None

    async def snapshot(thread_id: str) -> dict:
        state = await app.state.graph.aget_state({"configurable": {"thread_id": thread_id}})
        return {
            "thread_id": thread_id,
            "pending_nodes": list(state.next),
            "interrupts": [{"id": item.id, "request": item.value} for item in state.interrupts],
            "summary": state.values.get("public_summary"),
        }

    async def events(thread_id: str, principal: Principal, input_value):
        from langgraph.types import Command

        sequence = 0
        config = {"configurable": {"thread_id": thread_id}, "recursion_limit": 100}
        context = AuthorizedContext(
            principal.customer_id, principal.principal_id, principal.role, app.state.registry.ledger
        )
        try:
            async with app.state.registry.guard(thread_id):
                if isinstance(input_value, dict):
                    current = await snapshot(thread_id)
                    if current["interrupts"] or current["summary"] or current["pending_nodes"]:
                        yield encode_event(
                            "error",
                            {"message": "Thread changed; refresh before running."},
                            sequence,
                        )
                        return
                if isinstance(input_value, ResumeThread):
                    current = await snapshot(thread_id)
                    pending = {item["id"]: item["request"] for item in current["interrupts"]}
                    if input_value.interrupt_id not in pending:
                        yield encode_event(
                            "error",
                            {"message": "Stale approval; refresh the thread snapshot."},
                            sequence,
                        )
                        return
                    request = pending[input_value.interrupt_id]
                    if (
                        request.get("kind") in {"payout_approval", "payment_approval"}
                        and principal.role != "adjuster"
                    ):
                        yield encode_event(
                            "error", {"message": "An adjuster must make this decision."}, sequence
                        )
                        return
                    payload = input_value.model_dump(exclude={"interrupt_id"}, exclude_none=True)
                    input_value = Command(resume={input_value.interrupt_id: payload})
                async for part in app.state.graph.astream(
                    input_value,
                    config,
                    context=context,
                    stream_mode=["updates", "messages", "custom"],
                    subgraphs=True,
                    version="v2",
                ):
                    if part["type"] == "updates":
                        for node in part["data"]:
                            if node != "__interrupt__":
                                sequence += 1
                                yield encode_event("progress", {"node": node}, sequence)
                    elif part["type"] == "messages":
                        chunk, metadata = part["data"]
                        # Only explicitly public nodes may expose generated text.
                        if metadata.get("langgraph_node") == "draft_letter" and isinstance(
                            chunk.content, str
                        ):
                            sequence += 1
                            yield encode_event("token", {"text": chunk.content}, sequence)
                sequence += 1
                yield encode_event("snapshot", await snapshot(thread_id), sequence)
        except BusyThread:
            yield encode_event(
                "error",
                {"message": "Another run is active; refresh before retrying."},
                sequence + 1,
            )
        except (ValueError, PermissionError):
            yield encode_event(
                "error",
                {"message": "The request failed validation or authorization."},
                sequence + 1,
            )

    @app.get("/health")
    async def health():
        return {"status": "ready" if app.state.graph is not None else "starting"}

    @app.post("/threads", status_code=201)
    async def create_thread(body: CreateThread, principal: identity):
        try:
            await app.state.registry.create(
                body.thread_id, principal, load_submission(body.submission)
            )
        except PermissionError:
            raise HTTPException(403, "Claim is unavailable to this customer") from None
        except ValueError:
            raise HTTPException(409, "Thread already exists") from None
        return {"thread_id": body.thread_id}

    @app.get("/threads/{thread_id}")
    async def get_thread(thread_id: str, principal: identity):
        await ownership(thread_id, principal)
        return await snapshot(thread_id)

    @app.post("/threads/{thread_id}/run")
    async def run_thread(thread_id: str, principal: identity):
        claim = await ownership(thread_id, principal)
        state = await snapshot(thread_id)
        # Reconnection uses a snapshot and a resume/run request, not replay of SSE event IDs.
        if state["interrupts"] or state["summary"]:
            raise HTTPException(
                409, "Read the current snapshot before resuming or starting another claim"
            )
        input_value = (
            None
            if state["pending_nodes"]
            else {"claim": claim, "requested_on": "2026-01-01", "audit": [], "findings": []}
        )
        return StreamingResponse(
            events(thread_id, principal, input_value),
            media_type="text/event-stream",
            headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
        )

    @app.post("/threads/{thread_id}/resume")
    async def resume_thread(thread_id: str, body: ResumeThread, principal: identity):
        await ownership(thread_id, principal)
        current = await snapshot(thread_id)
        pending = {item["id"]: item["request"] for item in current["interrupts"]}
        if body.interrupt_id not in pending:
            raise HTTPException(409, "Stale interrupt; refresh the thread")
        if (
            pending[body.interrupt_id].get("kind") in {"payout_approval", "payment_approval"}
            and principal.role != "adjuster"
        ):
            raise HTTPException(403, "An adjuster must make this decision")
        return StreamingResponse(events(thread_id, principal, body), media_type="text/event-stream")

    return app
