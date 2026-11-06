"""Extend subgraph persistence: Include nested updates when streaming subgraphs.. Run this file with Python. No live model or network."""

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


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    graph = build_graph(case["persistent_child"])
    config = {"configurable": {"thread_id": case["claim_id"]}}
    parts = list(
        graph.stream(
            {"claim_id": case["claim_id"], "checks": 0},
            config,
            stream_mode="updates",
            subgraphs=False,
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
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
