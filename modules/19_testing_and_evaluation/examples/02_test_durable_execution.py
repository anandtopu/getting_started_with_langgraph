"""Assert pause/resume, checkpoint transitions, and reducer algebra. No LLM.

Run: uv run python modules/19_testing_and_evaluation/examples/02_test_durable_execution.py
Expected: no approval before resume; rejected claims remain rejected; findings merge associatively.
"""

from langgraph.types import Command

from common.copilot import v03
from common.copilot.v01 import merge_findings
from common.data import load_submission
from common.pretty import print_state

DEFAULT_CASE = {"approved": False, "groups": [["receipt"], ["estimate", "receipt"], ["policy"]]}


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
    print_state(run())


if __name__ == "__main__":
    main()
