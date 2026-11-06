"""Extend delta channels beta: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from typing import Annotated, TypedDict

from langgraph.channels import DeltaChannel
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"notes": ["intake", "policy", "estimate"], "snapshot_frequency": 2}


def merge_batches(current, writes):
    result = list(current or [])
    for write in writes:
        result.extend(write)
    return result


def build_graph(frequency=2):
    class State(TypedDict):
        note: str
        notes: Annotated[list[str], DeltaChannel(merge_batches, snapshot_frequency=frequency)]

    graph = StateGraph(State)
    graph.add_node("record_note", lambda state: {"notes": [state["note"]]})
    graph.add_edge(START, "record_note")
    graph.add_edge("record_note", END)
    return graph.compile(checkpointer=InMemorySaver())


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    graph = build_graph(case["snapshot_frequency"])
    config = {"configurable": {"thread_id": "delta-claim"}}
    for note in case["notes"]:
        graph.invoke({"note": note}, config, version="v2")
    values = graph.get_state(config).values
    return {
        "notes": values.get("notes", []),
        "reconstructed": values.get("notes", []) == case["notes"],
        "beta": True,
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
