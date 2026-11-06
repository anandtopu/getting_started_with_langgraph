"""Trace command routes: A competing static edge schedules an extra acknowledgment.. Run this file with Python. No live model or network."""

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
    graph.add_edge("triage", "acknowledge")
    graph.add_edge("review", END)
    graph.add_edge("acknowledge", END)
    return graph.compile()


def scenario(case: dict | None = None) -> dict:
    return (
        build_graph()
        .invoke({**(DEFAULT_CASE if case is None else case), "visited": []}, version="v2")
        .value
    )


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"claim_id": "CLM-0001", "suspicious": True},
        {"claim_id": "CLM-0001", "suspicious": False},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "A competing static edge schedules an extra acknowledgment.",
    }


if __name__ == "__main__":
    main()
