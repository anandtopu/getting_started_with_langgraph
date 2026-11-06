"""Exercise the real API in process with explicit synthetic credentials, without sockets."""

import asyncio
from pathlib import Path
from tempfile import TemporaryDirectory

import httpx

from apps.api import create_app
from common.copilot.v11 import build_graph
from common.service import Principal, ThreadRegistry
from common.sse import decode_events

CUSTOMER = "synthetic-customer-token"
ADJUSTER = "synthetic-adjuster-token"
OTHER = "synthetic-other-token"


async def exercise_api(approve=True, stale=False):
    with TemporaryDirectory(prefix="larkspur-api-") as directory:
        registry = ThreadRegistry(Path(directory) / "registry.db")
        app = create_app(
            build_graph(),
            registry,
            {
                CUSTOMER: Principal("customer", "CUS-0001", "customer"),
                ADJUSTER: Principal("adjuster", "CUS-0001", "adjuster"),
                OTHER: Principal("other", "CUS-0002", "customer"),
            },
        )
        headers = {"Authorization": "Bearer " + ADJUSTER}
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://in-process"
        ) as client:
            created = await client.post(
                "/threads", json={"thread_id": "demo", "submission": 1}, headers=headers
            )
            response = await client.post("/threads/demo/run", headers=headers)
            events = decode_events(response.text)
            pending = events[-1]["data"]["interrupts"][0]
            estimate = await client.post(
                "/threads/demo/resume",
                json={
                    "interrupt_id": pending["id"],
                    "document_id": "DOC-ESTIMATE",
                    "received_on": "2026-01-04",
                },
                headers=headers,
            )
            snapshot = decode_events(estimate.text)[-1]["data"]
            first_id = snapshot["interrupts"][0]["id"]
            forbidden = await client.post(
                "/threads/demo/resume",
                json={"interrupt_id": first_id, "approved": True},
                headers={"Authorization": "Bearer " + CUSTOMER},
            )
            while snapshot["interrupts"]:
                pending = snapshot["interrupts"][0]
                response = await client.post(
                    "/threads/demo/resume",
                    json={
                        "interrupt_id": pending["id"],
                        "approved": approve,
                        "coverage_confirmed": approve,
                    },
                    headers=headers,
                )
                frames = decode_events(response.text)
                if frames[-1]["event"] == "error":
                    raise RuntimeError(frames[-1]["data"]["message"])
                snapshot = frames[-1]["data"]
            foreign = await client.get(
                "/threads/demo", headers={"Authorization": "Bearer " + OTHER}
            )
            stale_response = await client.post(
                "/threads/demo/resume",
                json={"interrupt_id": first_id if stale else "missing", "approved": True},
                headers=headers,
            )
            return {
                "created": created.status_code,
                "foreign_status": foreign.status_code,
                "customer_approval_status": forbidden.status_code,
                "stale_status": stale_response.status_code,
                "effects": len(registry.ledger.rows()),
                "status": snapshot["summary"]["status"],
                "progress_events": sum(item["event"] == "progress" for item in events),
            }


def run_demo(approve=True, stale=False):
    return asyncio.run(exercise_api(approve, stale))
