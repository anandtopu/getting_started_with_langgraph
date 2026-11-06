"""Diagnose adjuster dashboard from execution evidence. Run this file with Python. No live model or network."""

from common.pretty import print_state
from common.sse import update_dashboard

DEFAULT_CASE = {"chunks": ["Estimate ", "received."], "submitted_id": "old-approval"}


def scenario(case: dict | None = None) -> dict:
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
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"chunks": ["Estimate ", "received."], "submitted_id": "old-approval"},
        {"chunks": ["Estimate ", "received."], "submitted_id": "current-approval"},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Replace the stale approval identity with the current snapshot.",
    }


if __name__ == "__main__":
    main()
