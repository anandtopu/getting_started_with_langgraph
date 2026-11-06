"""Diagnose channels and steps from execution evidence. Run this file with Python. No live model or network."""

from common.mini_graph import MiniGraph
from common.pretty import print_state

DEFAULT_CASE = {"documents": ["estimate", "receipt"]}


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    observed = []

    def worker(name):
        def inspect(state, resume):
            observed.append(len(state["findings"]) + 1)
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
    print_state(run())


def run() -> dict:
    observations = []
    for case in [{"documents": ["estimate", "receipt"]}, {"documents": []}]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Report the previous-boundary view seen by each worker.",
    }


if __name__ == "__main__":
    main()
