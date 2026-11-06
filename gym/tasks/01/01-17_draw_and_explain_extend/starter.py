"""Extend draw and explain: Add an opt-in eligibility node selected by eligibility_check=True. Preserve the original steps when absent; verify the new diagram connection and valid/invalid updates when enabled.. Run this file with Python. No live model or network."""

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
    eligible: bool


def receive(state: State) -> dict:
    return {"received": True}


def validate(state: State) -> dict:
    return {"valid": bool(state["description"].strip())}


def acknowledge(state: State) -> dict:
    return {"acknowledged": state["received"]}


def check_eligibility(state: State) -> dict:
    return {"eligible": True}


def build_graph(include_eligibility=False):
    graph = StateGraph(State)
    for name, node in (("receive", receive), ("validate", validate), ("acknowledge", acknowledge)):
        graph.add_node(name, node)
    graph.add_edge(START, "receive")
    graph.add_edge("receive", "validate")
    if include_eligibility:
        graph.add_node("check_eligibility", check_eligibility)
        graph.add_edge("validate", "check_eligibility")
        graph.add_edge("check_eligibility", "acknowledge")
    else:
        graph.add_edge("validate", "acknowledge")
    graph.add_edge("acknowledge", END)
    return graph.compile()


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    graph = build_graph(bool((case or {}).get("eligibility_check", False)))
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
