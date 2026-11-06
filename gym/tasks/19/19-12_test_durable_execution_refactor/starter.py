"""Refactor test durable execution: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

from langgraph.types import Command

from common.copilot import v03
from common.copilot.v01 import merge_findings
from common.data import load_submission
from common.pretty import print_state

DEFAULT_CASE = {"approved": False, "groups": [["receipt"], ["estimate", "receipt"], ["policy"]]}


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    graph = v03.build_graph()
    config = {"configurable": {"thread_id": "durable-test"}}
    claim = {**load_submission(1), "amount_cents": 600000}
    paused = graph.invoke({"claim": claim, "audit": [], "findings": []}, config, version="v2")
    before = graph.get_state(config)
    resumed = graph.invoke(Command(resume={"approved": case["approved"]}), config, version="v2")
    a, b, c = case["groups"]
    return {
        "paused": len(paused.interrupts) == 1,
        "pending_before": list(before.next),
        "pending_after": list(graph.get_state(config).next),
        "approved": resumed.value["approved"],
        "associative": merge_findings(merge_findings(a, b), c)
        == merge_findings(a, merge_findings(b, c)),
        "merged": merge_findings(merge_findings(a, b), c),
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
