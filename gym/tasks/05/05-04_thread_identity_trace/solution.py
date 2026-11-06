"""Diagnose thread identity from execution evidence. Run this file with Python. No live model or network."""

import operator
from typing import Annotated, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"first_id": "CLM-0001", "second_id": "CLM-0002"}


class State(TypedDict):
    claim_id: str
    notes: Annotated[list[str], operator.add]
    status: str


def save_note(state: State) -> dict:
    return {"status": "recorded"}


def thread_config(claim_id: str) -> dict:
    return {"configurable": {}}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("save_note", save_note)
    graph.add_edge(START, "save_note")
    graph.add_edge("save_note", END)
    return graph.compile(checkpointer=InMemorySaver())


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    graph = build_graph()
    first = thread_config(case["first_id"])
    second = thread_config(case["second_id"])
    graph.invoke({"claim_id": case["first_id"], "notes": ["received"]}, first, version="v2")
    graph.invoke({"claim_id": case["second_id"], "notes": ["other customer"]}, second, version="v2")
    result = graph.invoke({"notes": ["estimate attached"]}, first, version="v2").value
    return {"first_notes": result["notes"], "second_notes": graph.get_state(second).values["notes"]}


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"first_id": "CLM-0001", "second_id": "CLM-0002"},
        {"first_id": "CLM-A", "second_id": "CLM-B"},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "A persisted invocation needs an explicit thread identifier.",
    }


if __name__ == "__main__":
    main()
