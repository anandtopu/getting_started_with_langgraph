"""Observe barrier snapshots in a small educational runner. No LLM.

Run: uv run python modules/bonus/B3_mini_langgraph/examples/01_channels_and_steps.py
Expected: both document workers see zero prior findings; the summary sees both writes.
"""

from common.mini_graph import MiniGraph
from common.pretty import print_state

DEFAULT_CASE = {"documents": ["estimate", "receipt"]}


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
    print_state(run())


if __name__ == "__main__":
    main()
