"""Refactor v2 stream parts: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.config import get_stream_writer
from langgraph.graph import END, START, StateGraph
from langgraph.types import interrupt

from common.pretty import print_state, print_stream

DEFAULT_CASE = {"claim_id": "CLM-0001", "review": False}


class State(TypedDict):
    claim_id: str
    review: bool
    status: str


def receive(state: State) -> dict:
    get_stream_writer()({"phase": "received", "claim_id": state["claim_id"]})
    return {"status": "received"}


def validate(state: State) -> dict:
    if state["review"]:
        interrupt({"kind": "review", "claim_id": state["claim_id"]})
    return {"status": "validated"}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("receive", receive)
    graph.add_node("validate", validate)
    graph.add_edge(START, "receive")
    graph.add_edge("receive", "validate")
    graph.add_edge("validate", END)
    return graph.compile(checkpointer=InMemorySaver())


def summarize_part(part: dict) -> dict:
    result = {"type": part["type"], "namespace": list(part["ns"])}
    if part["type"] == "updates":
        result["nodes"] = sorted(part["data"])
    elif part["type"] == "values":
        result["status"] = part["data"].get("status", "input")
        result["interrupts"] = len(part.get("interrupts", ()))
    elif part["type"] == "custom":
        result["phase"] = part["data"]["phase"]
    else:
        result["event"] = part["data"]["type"]
    return result


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
    parts = build_graph().stream(
        dict(case),
        {"configurable": {"thread_id": "stream-claim"}},
        stream_mode=["updates", "values", "custom", "debug"],
        version="v2",
    )
    return {"parts": [summarize_part(part) for part in parts]}


def main() -> None:
    try:
        print_state(run())
        for part in build_graph().stream(
            DEFAULT_CASE,
            {"configurable": {"thread_id": "print-claim"}},
            stream_mode="updates",
            version="v2",
        ):
            print_stream(part)
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
