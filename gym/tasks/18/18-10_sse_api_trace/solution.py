"""Trace sse api: Carry a rejection through the authenticated workflow.. Run this file with Python. No live model or network."""

from common.app_demo import run_demo
from common.pretty import print_state
from common.sse import decode_events, encode_event

DEFAULT_CASE = {"approved": True, "stale": True, "note": "Estimate\nreceived"}


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    frame = encode_event("progress", {"node": case["note"]}, 1)
    decoded = decode_events(frame)
    result = run_demo(approve=True, stale=case["stale"])
    return {
        **result,
        "framing_roundtrip": decoded[0]["data"]["node"] == case["note"],
        "frame_count": len(decoded),
    }


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"approved": True, "note": "Estimate\nreceived", "stale": True},
        {"approved": False, "note": "Estimate\nreceived", "stale": True},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Carry a rejection through the authenticated workflow.",
    }


if __name__ == "__main__":
    main()
