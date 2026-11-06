"""Exercise the running Compose API before and after a real server restart."""

import argparse
import json
import os
from pathlib import Path

import httpx

from common.sse import decode_events


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["start", "resume"])
    args = parser.parse_args()
    headers = {"Authorization": "Bearer " + os.environ["LARKSPUR_ADJUSTER_TOKEN"]}
    saved = Path("tmp/deployment-thread.json")
    saved.parent.mkdir(exist_ok=True)
    with httpx.Client(base_url="http://127.0.0.1:8000", headers=headers, timeout=120) as client:
        assert client.get("/health").status_code == 200
        if args.stage == "start":
            created = client.post("/threads", json={"thread_id": "restart-check", "submission": 1})
            assert created.status_code == 201, created.text
            response = client.post("/threads/restart-check/run")
            assert response.status_code == 200, response.text
            events = decode_events(response.text)
            assert not any(event["event"] == "error" for event in events), events
            snapshot = events[-1]["data"]
            assert snapshot["interrupts"][0]["request"]["kind"] == "estimate_wait", snapshot
            saved.write_text(json.dumps(snapshot), "utf-8")
        else:
            previous = json.loads(saved.read_text("utf-8"))
            snapshot = client.get("/threads/restart-check").json()
            assert snapshot["interrupts"] == previous["interrupts"], snapshot
            first = snapshot["interrupts"][0]["id"]
            while snapshot["interrupts"]:
                pending = snapshot["interrupts"][0]
                payload = {"interrupt_id": pending["id"]}
                if pending["request"]["kind"] == "estimate_wait":
                    payload.update(document_id="DOC-ESTIMATE", received_on="2026-01-04")
                else:
                    payload.update(approved=True, coverage_confirmed=True)
                    denied = client.post(
                        "/threads/restart-check/resume",
                        json=payload,
                        headers={
                            "Authorization": "Bearer " + os.environ["LARKSPUR_CUSTOMER_TOKEN"]
                        },
                    )
                    assert denied.status_code == 403, denied.text
                response = client.post("/threads/restart-check/resume", json=payload)
                assert response.status_code == 200, response.text
                events = decode_events(response.text)
                assert not any(event["event"] == "error" for event in events), events
                snapshot = events[-1]["data"]
            assert snapshot["summary"]["status"] == "recorded", snapshot
            assert (
                client.post(
                    "/threads/restart-check/resume", json={"interrupt_id": first, "approved": True}
                ).status_code
                == 409
            )
    print("PASS Compose", args.stage)


if __name__ == "__main__":
    main()
