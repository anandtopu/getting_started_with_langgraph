"""Fix approve or reject: An interrupt needs persistence to resume the saved task.. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from common.pretty import print_state

DEFAULT_CASE = {"amount_cents": 600000, "decision": {"approved": True}}


class State(TypedDict):
    amount_cents: int
    status: str


def review(state: State) -> dict:
    response = interrupt({"kind": "payout_review", "amount_cents": state["amount_cents"]})
    if not isinstance(response, dict) or type(response.get("approved")) is not bool:
        raise ValueError("Approval must contain an approved boolean")
    return {"status": "approved" if response["approved"] else "rejected"}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("review", review)
    graph.add_edge(START, "review")
    graph.add_edge("review", END)
    return graph.compile(checkpointer=InMemorySaver())


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    graph = build_graph()
    config = {"configurable": {"thread_id": "review-claim"}}
    paused = graph.invoke({"amount_cents": case["amount_cents"]}, config, version="v2")
    completed = graph.invoke(Command(resume=case["decision"]), config, version="v2")
    return {
        "prompts": [item.value for item in paused.interrupts],
        "status": completed.value["status"],
        "remaining": len(completed.interrupts),
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
