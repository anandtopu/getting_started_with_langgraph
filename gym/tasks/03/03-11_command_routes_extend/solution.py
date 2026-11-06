"""Extend command routes: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

import operator
from typing import Annotated, Literal, TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import Command

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "suspicious": True}


class State(TypedDict):
    claim_id: str
    suspicious: bool
    reason: str
    visited: Annotated[list[str], operator.add]


def triage(state: State) -> Command[Literal["review", "acknowledge"]]:
    destination = "review" if state["suspicious"] else "acknowledge"
    return Command(
        update={"reason": "indicator" if state["suspicious"] else "routine"}, goto=destination
    )


def review(state: State) -> dict:
    return {"visited": ["review"]}


def acknowledge(state: State) -> dict:
    return {"visited": ["acknowledge"]}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("triage", triage)
    graph.add_node("review", review)
    graph.add_node("acknowledge", acknowledge)
    graph.add_edge(START, "triage")
    graph.add_edge("review", END)
    graph.add_edge("acknowledge", END)
    return graph.compile()


def run(case: dict | None = None) -> dict:
    return (
        build_graph()
        .invoke({**(DEFAULT_CASE if case is None else case), "visited": []}, version="v2")
        .value
    )


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
