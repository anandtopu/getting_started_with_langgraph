"""Diagnose wire pipeline from execution evidence. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "description": " Water leak ", "steps": []}


class State(TypedDict):
    claim_id: str
    description: str
    status: str
    acknowledged: bool
    steps: list[str]


def normalize(state: State) -> dict:
    return {"description": state["description"].strip(), "steps": [*state["steps"], "normalize"]}


def validate(state: State) -> dict:
    return {
        "status": "ready" if state["description"] else "needs_information",
        "steps": [*state["steps"], "validate"],
    }


def acknowledge(state: State) -> dict:
    return {"acknowledged": True, "steps": [*state["steps"], "acknowledge"]}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("normalize", normalize)
    graph.add_node("validate", validate)
    graph.add_node("acknowledge", acknowledge)
    graph.add_edge(START, "normalize")
    graph.add_edge("normalize", "acknowledge")
    graph.add_edge("validate", "acknowledge")
    graph.add_edge("acknowledge", END)
    return graph.compile()


def run(case: dict | None = None) -> dict:
    return build_graph().invoke(dict(DEFAULT_CASE if case is None else case), version="v2").value


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
