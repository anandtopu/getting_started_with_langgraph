"""Predict v2 stream parts across the declared cases. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.config import get_stream_writer
from langgraph.graph import END, START, StateGraph
from langgraph.types import interrupt

from common.pretty import print_state

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


def scenario(case: dict | None = None) -> dict:
    parts = build_graph().stream(
        dict(DEFAULT_CASE if case is None else case),
        {"configurable": {"thread_id": "stream-claim"}},
        stream_mode=["updates", "values", "custom", "debug"],
        version="v2",
    )
    return {"parts": [summarize_part(part) for part in parts]}


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"claim_id": "CLM-0001", "review": False},
        {"claim_id": "CLM-0001", "review": True},
        {"claim_id": "CLM-0040", "review": False},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
