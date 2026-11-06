"""A Streamlit session must not retain another claim's streamed text."""

import httpx
import pytest

pytest.importorskip("streamlit")
from streamlit.testing.v1 import AppTest

from common.config import ROOT


def test_switching_threads_discards_the_cached_stream(monkeypatch):
    original_client = httpx.Client

    def handler(request):
        return httpx.Response(
            200,
            json={
                "thread_id": request.url.path.split("/")[-1],
                "summary": None,
                "interrupts": [],
                "pending_nodes": [],
            },
        )

    def client(**kwargs):
        return original_client(transport=httpx.MockTransport(handler), **kwargs)

    monkeypatch.setattr(httpx, "Client", client)
    app = AppTest.from_file(str(ROOT / "apps/dashboard.py"), default_timeout=20)
    app.run()
    app.text_input[0].set_value("first-adjuster-token")
    app.text_input[1].set_value("claim-a")
    app.run()
    assert not app.exception
    app.session_state["view"] = {"text": "private previous claim text"}
    app.text_input[1].set_value("claim-b").run()
    assert not app.exception
    assert "view" not in app.session_state
    assert all("private previous" not in item.value for item in app.markdown)
