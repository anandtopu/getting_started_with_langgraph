"""Diagnose draw and explain from execution evidence. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "description": "Pipe burst"}


class State(TypedDict):
    claim_id: str
    description: str
    received: bool
    valid: bool
    acknowledged: bool


def receive(state: State) -> dict:
    return {"received": True}


def validate(state: State) -> dict:
    return {"valid": bool(state["description"].strip())}


def acknowledge(state: State) -> dict:
    return {"acknowledged": state["received"]}


def build_graph():
    graph = StateGraph(State)
    for name, node in (("receive", receive), ("validate", validate), ("acknowledge", acknowledge)):
        graph.add_node(name, node)
    graph.add_edge(START, "receive")
    graph.add_edge("receive", "validate")
    graph.add_edge("validate", END)
    graph.add_edge("acknowledge", END)
    return graph.compile()


def run(case: dict | None = None) -> dict:
    graph = build_graph()
    parts = list(
        graph.stream(
            dict(DEFAULT_CASE if case is None else case), stream_mode="updates", version="v2"
        )
    )
    return {
        "steps": [next(iter(part["data"])) for part in parts],
        "updates": [part["data"] for part in parts],
    }


def main() -> None:
    try:
        print_state(run())
        print(build_graph().get_graph().draw_mermaid())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
