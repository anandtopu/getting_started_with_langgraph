"""Refactor thread identity: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

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
    return {"configurable": {"thread_id": "claim:" + claim_id}}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("save_note", save_note)
    graph.add_edge(START, "save_note")
    graph.add_edge("save_note", END)
    return graph.compile(checkpointer=InMemorySaver())


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
    graph = build_graph()
    first = thread_config(case["first_id"])
    second = thread_config(case["second_id"])
    graph.invoke({"claim_id": case["first_id"], "notes": ["received"]}, first, version="v2")
    graph.invoke({"claim_id": case["second_id"], "notes": ["other customer"]}, second, version="v2")
    result = graph.invoke({"notes": ["estimate attached"]}, first, version="v2").value
    return {"first_notes": result["notes"], "second_notes": graph.get_state(second).values["notes"]}


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
