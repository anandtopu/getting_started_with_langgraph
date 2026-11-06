"""Trace bounded rechecks: Without a changing retry counter, the graph reaches its recursion limit.. Run this file with Python. No live model or network."""

import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"history": [False, False, True], "budget": 3}


class State(TypedDict):
    history: list[bool]
    budget: int
    attempts: int
    status: str
    trace: Annotated[list[str], operator.add]


def check_documents(state: State) -> dict:
    index = state["attempts"]
    received = index < len(state["history"]) and state["history"][index]
    exhausted = index + 1 >= state["budget"]
    status = "ready" if received else "exhausted" if exhausted else "waiting"
    return {
        "attempts": index,
        "status": status,
        "trace": ["received" if received else "missing"],
    }


def next_check(state: State) -> str:
    return END if state["status"] in {"ready", "exhausted"} else "check_documents"


def build_graph():
    graph = StateGraph(State)
    graph.add_node("check_documents", check_documents)
    graph.add_edge(START, "check_documents")
    graph.add_conditional_edges(
        "check_documents", next_check, {"check_documents": "check_documents", END: END}
    )
    return graph.compile()


def scenario(case: dict | None = None) -> dict:
    values = dict(DEFAULT_CASE if case is None else case)
    limit = values.pop("recursion_limit", 30)
    if type(values["budget"]) is not int or values["budget"] < 1:
        raise ValueError("A recheck budget must be a positive integer")
    return (
        build_graph()
        .invoke({**values, "attempts": 0, "trace": []}, {"recursion_limit": limit}, version="v2")
        .value
    )


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [{"budget": 3, "history": [False, False, True]}, {"budget": 3, "history": [True]}]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Without a changing retry counter, the graph reaches its recursion limit.",
    }


if __name__ == "__main__":
    main()
