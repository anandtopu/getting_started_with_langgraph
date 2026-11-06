"""Independent HTTP regressions for malformed decisions and cross-claim inputs."""

from types import SimpleNamespace

import httpx
import pytest

pytest.importorskip("fastapi")

from apps.api import create_app
from common.copilot.v11 import build_graph
from common.service import Principal, ThreadRegistry
from common.sse import decode_events


@pytest.fixture
def api(tmp_path):
    registry = ThreadRegistry(tmp_path / "registry.db")
    graph = build_graph()
    token = "adjuster-secret-token"
    app = create_app(graph, registry, {token: Principal("adjuster", "CUS-0019", "adjuster")})
    return app, registry, token


async def test_non_ascii_bearer_is_unauthorized_instead_of_server_error(api):
    app, _, _ = api
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/threads/claim", headers={b"Authorization": b"Bearer \xff"})
    assert response.status_code == 401


async def test_missing_amount_finishes_without_payment_and_malformed_resume_can_be_retried(api):
    app, registry, token = api
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://test",
        headers={"Authorization": "Bearer " + token},
    ) as client:
        assert (
            await client.post("/threads", json={"thread_id": "incomplete", "submission": 19})
        ).status_code == 201
        initial = await client.post("/threads/incomplete/run")
        pending = decode_events(initial.text)[-1]["data"]["interrupts"][0]
        malformed = await client.post(
            "/threads/incomplete/resume",
            json={"interrupt_id": pending["id"], "document_id": "DOC-19"},
        )
        assert malformed.status_code == 422
        retried = await client.post(
            "/threads/incomplete/resume",
            json={
                "interrupt_id": pending["id"],
                "document_id": "DOC-19",
                "received_on": "2026-01-04",
            },
        )
        snapshot = decode_events(retried.text)[-1]["data"]
        assert snapshot["summary"]["status"] == "not_approved"
        assert snapshot["interrupts"] == [] and registry.ledger.rows() == []


async def test_unexpected_stream_failure_is_public_and_releases_lease(api, monkeypatch):
    app, registry, token = api

    async def fail(*args, **kwargs):
        raise RuntimeError("private provider detail")
        yield  # An async generator has the same streaming protocol as the graph.

    monkeypatch.setattr(app.state.graph, "astream", fail)
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://test",
        headers={"Authorization": "Bearer " + token},
    ) as client:
        await client.post("/threads", json={"thread_id": "failed", "submission": 19})
        response = await client.post("/threads/failed/run")
    assert decode_events(response.text)[-1]["event"] == "error"
    assert "private provider detail" not in response.text
    async with registry.guard("failed"):
        pass


async def test_recovery_rechecks_the_snapshot_after_taking_the_lease(api, monkeypatch):
    app, _, token = api
    reads, executions = [], []

    async def snapshot(*args, **kwargs):
        reads.append(True)
        if len(reads) == 1:
            return SimpleNamespace(next=("pending",), interrupts=(), values={})
        return SimpleNamespace(
            next=(), interrupts=(), values={"public_summary": {"status": "recorded"}}
        )

    async def execute(*args, **kwargs):
        executions.append(True)
        yield {}

    monkeypatch.setattr(app.state.graph, "aget_state", snapshot)
    monkeypatch.setattr(app.state.graph, "astream", execute)
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://test",
        headers={"Authorization": "Bearer " + token},
    ) as client:
        await client.post("/threads", json={"thread_id": "racing", "submission": 19})
        response = await client.post("/threads/racing/run")
    assert executions == []
    assert "Thread changed" in decode_events(response.text)[-1]["data"]["message"]
