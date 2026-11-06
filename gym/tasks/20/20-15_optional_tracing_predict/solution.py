"""Predict optional tracing across the declared cases. Run this file with Python. No live model or network."""

from langsmith import tracing_context

from common.copilot.v02 import build_graph
from common.data import load_submission
from common.pretty import print_state

DEFAULT_CASE = {"corrected_cents": 50000}


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    graph = build_graph()
    config = {
        "configurable": {"thread_id": "trace-claim"},
        "metadata": {"course": "larkspur", "synthetic": True},
    }
    with tracing_context(enabled=False):
        graph.invoke(
            {"claim": {**load_submission(1), "amount_cents": 600000}, "audit": [], "findings": []},
            config,
            version="v2",
        )
        history = list(graph.get_state_history(config))
        before_route = next(item for item in history if "route" in item.next)
        fork = graph.update_state(
            before_route.config,
            {"claim": {**before_route.values["claim"], "amount_cents": case["corrected_cents"]}},
        )
        result = graph.invoke(None, fork, version="v2")
    return {
        "original_route": history[0].values["route"],
        "forked_route": result.value["route"],
        "fork_pending": list(before_route.next),
        "history_retained": len(list(graph.get_state_history(config))) > len(history),
        "remote_tracing": False,
    }


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"corrected_cents": 50000},
        {"corrected_cents": 600000},
        {"corrected_cents": 100001},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
