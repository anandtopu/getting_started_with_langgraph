"""Fix safe reentry: Effects before interrupt repeat when the node restarts.. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "approved": True}


class State(TypedDict):
    claim_id: str
    approved: bool
    notification_key: str


def build_graph(entries: list[str], notifications: dict[str, str]):
    def review(state: State) -> dict:
        entries.append("review")
        decision = interrupt({"kind": "approval", "claim_id": state["claim_id"]})
        if type(decision) is not bool:
            raise ValueError("Expected a boolean approval")
        return {"approved": decision}

    def notify(state: State) -> dict:
        key = state["claim_id"] + ":approval:v1"
        if state["approved"]:
            notifications.setdefault(key, "Synthetic approval notification")
        return {"notification_key": key}

    graph = StateGraph(State)
    graph.add_node("review", review)
    graph.add_node("notify", notify)
    graph.add_edge(START, "review")
    graph.add_edge("review", "notify")
    graph.add_edge("notify", END)
    return graph.compile(checkpointer=InMemorySaver())


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    entries, notifications = [], {}
    graph = build_graph(entries, notifications)
    config = {"configurable": {"thread_id": case["claim_id"]}}
    graph.invoke({"claim_id": case["claim_id"]}, config, version="v2")
    before = len(notifications)
    result = graph.invoke(Command(resume=case["approved"]), config, version="v2").value
    return {
        "entries": len(entries),
        "before_approval": before,
        "notifications": len(notifications),
        "approved": result["approved"],
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
