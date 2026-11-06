"""Extend channels and steps: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

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


def run_batch(cases: list[dict]) -> list[dict]:
    """Preview independent claims in order; one rejected input must not lose its siblings.

    This sequential interface favors isolation over throughput. It is not a shared
    checkpoint thread or a promise of transaction atomicity.
    """
    from copy import deepcopy

    from common.pretty import safe_value

    results = []
    for case in cases:
        try:
            results.append({"value": safe_value(run(deepcopy(case)))})
        except Exception as error:
            results.append({"error": type(error).__name__})
    return results


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
