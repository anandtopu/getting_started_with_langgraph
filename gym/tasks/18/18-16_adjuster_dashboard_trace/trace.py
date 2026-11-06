"""Trace adjuster dashboard: Replace the stale approval identity with the current snapshot.. Run this file with Python. No live model or network."""

from common.pretty import print_state
from common.sse import update_dashboard

DEFAULT_CASE = {"chunks": ["Estimate ", "received."], "submitted_id": "old-approval"}


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    state = {"progress": [], "pending": [{"id": "old-approval"}]}
    state = update_dashboard(state, {"event": "progress", "data": {"node": "review_documents"}})
    for chunk in case["chunks"]:
        state = update_dashboard(state, {"event": "token", "data": {"text": chunk}})
    state = update_dashboard(
        state,
        {
            "event": "snapshot",
            "data": {"interrupts": [{"id": "old-approval", "request": {"amount_cents": 600000}}]},
        },
    )
    allowed = case["submitted_id"] in {item["id"] for item in state["pending"]}
    return {
        "progress": state["progress"],
        "text": state.get("text", ""),
        "current_ids": [item["id"] for item in state["pending"]],
        "can_submit": allowed,
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
