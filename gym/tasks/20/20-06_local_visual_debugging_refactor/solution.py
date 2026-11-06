"""Refactor local visual debugging: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

import json

from common.config import ROOT
from common.copilot.v03 import build_graph
from common.data import load_submission
from common.pretty import print_state

DEFAULT_CASE = {"amount_cents": 600000, "reported_route": "fast_track"}


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
    config = json.loads((ROOT / "langgraph.json").read_text("utf-8"))
    source, symbol = config["graphs"]["claims"].split(":")
    graph = build_graph()
    diagram = graph.get_graph().draw_mermaid()
    result = graph.invoke(
        {
            "claim": {**load_submission(1), "amount_cents": case["amount_cents"]},
            "audit": [],
            "findings": [],
        },
        {"configurable": {"thread_id": "debug-claim"}},
        version="v2",
    )
    return {
        "export_exists": (ROOT / source).is_file(),
        "symbol": symbol,
        "diagram_has_approval": "approve_claim" in diagram,
        "actual_route": result.value["route"],
        "misrouted": result.value["route"] != case["reported_route"],
        "paused": bool(result.interrupts),
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
