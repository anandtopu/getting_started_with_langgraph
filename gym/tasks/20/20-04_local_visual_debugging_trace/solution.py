"""Diagnose local visual debugging from execution evidence. Run this file with Python. No live model or network."""

import json

from common.config import ROOT
from common.copilot.v03 import build_graph
from common.data import load_submission
from common.pretty import print_state

DEFAULT_CASE = {"amount_cents": 600000, "reported_route": "fast_track"}


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    config = json.loads((ROOT / "langgraph.json").read_text("utf-8"))
    source, symbol = config["graphs"]["claims"].split(":")
    graph = build_graph()
    diagram = graph.get_graph().draw_mermaid()
    result = graph.invoke(
        {"claim": {**load_submission(1), "amount_cents": 0}, "audit": [], "findings": []},
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
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"amount_cents": 600000, "reported_route": "fast_track"},
        {"amount_cents": 100000, "reported_route": "fast_track"},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Debug the supplied claim amount rather than a substituted value.",
    }


if __name__ == "__main__":
    main()
