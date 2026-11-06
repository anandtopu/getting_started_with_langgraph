"""Refactor sse api: Compare the payload field after decoding, not its event category.. Run this file with Python. No live model or network."""

from common.app_demo import run_demo
from common.pretty import print_state
from common.sse import decode_events, encode_event

DEFAULT_CASE = {"approved": True, "stale": True, "note": "Estimate\nreceived"}


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    frame = encode_event("progress", {"node": case["note"]}, 1)
    decoded = decode_events(frame)
    result = run_demo(approve=case["approved"], stale=case["stale"])
    return {
        **result,
        "framing_roundtrip": decoded[0]["event"] == case["note"],
        "frame_count": len(decoded),
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
