"""Refactor channels and steps: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

from common.mini_graph import MiniGraph
from common.pretty import print_state

DEFAULT_CASE = {"documents": ["estimate", "receipt"]}


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    observed = []

    def worker(name):
        def inspect(state, resume):
            observed.append(len(state["findings"]))
            return {"findings": ["reviewed:" + name]}

        return inspect

    nodes = {name: worker(name) for name in case["documents"]}
    nodes["summary"] = lambda state, resume: {"count": len(state["findings"])}
    graph = MiniGraph(
        nodes,
        {name: ["summary"] for name in case["documents"]},
        case["documents"] or ["summary"],
        {"findings": lambda old, new: (old or []) + new},
    )
    result = graph.run({"findings": []})
    return {
        "worker_views": observed,
        "findings": sorted(result.values["findings"]),
        "count": result.values["count"],
        "steps": result.step,
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
