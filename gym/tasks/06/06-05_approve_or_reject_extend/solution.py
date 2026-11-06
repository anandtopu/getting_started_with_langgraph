"""Extend approve or reject: Only a validated boolean authorizes this synthetic decision.. Run this file with Python. No live model or network."""

from typing import TypedDict

from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from common.pretty import print_state

DEFAULT_CASE = {"amount_cents": 600000, "decision": {"approved": True}}


class State(TypedDict):
    amount_cents: int
    status: str
    approved_by: str


def review(state: State, config: RunnableConfig) -> dict:
    response = interrupt({"kind": "payout_review", "amount_cents": state["amount_cents"]})
    adjuster = config["configurable"]["adjuster_id"]
    if adjuster not in {"ADJ-001", "ADJ-002"}:
        raise PermissionError("The trusted session is not an authorized adjuster")
    if not isinstance(response, dict) or type(response.get("approved")) is not bool:
        raise ValueError("Approval must contain an approved boolean")
    return {"status": "approved" if response["approved"] else "rejected", "approved_by": adjuster}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("review", review)
    graph.add_edge(START, "review")
    graph.add_edge("review", END)
    return graph.compile(checkpointer=InMemorySaver())


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    graph = build_graph()
    config = {
        "configurable": {
            "thread_id": "review-claim",
            "adjuster_id": case.get("adjuster_id", "ADJ-001"),
        }
    }
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
