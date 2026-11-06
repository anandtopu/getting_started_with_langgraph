"""Predict subgraph persistence across the declared cases. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "approved": False, "persistent_child": False}


class State(TypedDict):
    claim_id: str
    approved: bool
    checks: int


def build_graph(persistent_child: bool = False):
    def review(state: State) -> dict:
        decision = interrupt({"claim_id": state["claim_id"], "question": "Approve fraud review?"})
        if type(decision) is not bool:
            raise ValueError("Review requires a boolean")
        return {"approved": decision, "checks": state.get("checks", 0) + 1}

    child = StateGraph(State)
    child.add_node("review", review)
    child.add_edge(START, "review")
    child.add_edge("review", END)
    parent = StateGraph(State)
    parent.add_node("fraud", child.compile(checkpointer=True if persistent_child else None))
    parent.add_edge(START, "fraud")
    parent.add_edge("fraud", END)
    return parent.compile(checkpointer=InMemorySaver())


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    graph = build_graph(case["persistent_child"])
    config = {"configurable": {"thread_id": case["claim_id"]}}
    parts = list(
        graph.stream(
            {"claim_id": case["claim_id"], "checks": 0},
            config,
            stream_mode="updates",
            subgraphs=True,
            version="v2",
        )
    )
    snapshot = graph.get_state(config, subgraphs=True)
    child_state = snapshot.tasks[0].state
    result = graph.invoke(Command(resume=case["approved"]), config, version="v2")
    return {
        "child_pending": list(child_state.next),
        "child_claim": child_state.values["claim_id"],
        "nested_stream": any(part["ns"] for part in parts),
        "approved": result.value["approved"],
        "checks": result.value["checks"],
    }


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"approved": False, "claim_id": "CLM-0001", "persistent_child": False},
        {"approved": True, "claim_id": "CLM-0001", "persistent_child": False},
        {"approved": False, "claim_id": "CLM-0001", "persistent_child": True},
        {"approved": "yes", "claim_id": "CLM-0001", "persistent_child": False},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
