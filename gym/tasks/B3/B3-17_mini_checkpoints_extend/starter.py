"""Extend mini checkpoints: Read the archived snapshot rather than an externally modified copy.. Run this file with Python. No live model or network."""

from common.mini_graph import MiniGraph, Pause
from common.pretty import print_state

DEFAULT_CASE = {"approved": False, "claim_id": "CLM-0001"}


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case

    def review(state, resume):
        if resume is None:
            raise Pause({"claim_id": state["claim_id"], "question": "Approve?"})
        if type(resume) is not bool:
            raise ValueError("Expected boolean approval")
        return {"approved": resume}

    graph = MiniGraph({"review": review}, {}, ["review"])
    paused = graph.run({"claim_id": case["claim_id"]}, thread_id="A")
    graph.run({"claim_id": "CLM-0002"}, thread_id="B")
    result = graph.run(None, thread_id="A", resume=case["approved"])
    copy = graph.latest("A")
    copy.values["claim_id"] = "changed outside the runner"
    return {
        "request": paused.request,
        "approved": result.values["approved"],
        "other_pending": graph.latest("B").pending,
        "original_id": copy.values["claim_id"],
        "completed": not result.pending,
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
