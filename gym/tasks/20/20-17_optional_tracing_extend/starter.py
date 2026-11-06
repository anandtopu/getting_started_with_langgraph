"""Extend optional tracing: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from langsmith import tracing_context

from common.copilot.v02 import build_graph
from common.data import load_submission
from common.pretty import print_state

DEFAULT_CASE = {"corrected_cents": 50000}


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
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


def run_batch(cases: list[dict]) -> list[dict]:
    return []


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
