"""Fix collect and edit: Each interrupt must receive the response for its own request kind.. Run this file with Python. No live model or network."""

from datetime import date
from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from common.pretty import print_state

DEFAULT_CASE = {"loss_date": "2026-01-01", "approved_cents": 125000}


class State(TypedDict):
    claim_id: str
    loss_date: str
    approved_cents: int


def collect_date(state: State) -> dict:
    response = interrupt({"kind": "loss_date", "claim_id": state["claim_id"]})
    return {"loss_date": date.fromisoformat(response).isoformat()}


def edit_amount(state: State) -> dict:
    response = interrupt({"kind": "approved_cents", "claim_id": state["claim_id"]})
    if type(response) is not int or not 0 <= response <= 500000:
        raise ValueError("Edited amount must be integer cents within the proposal limit")
    return {"approved_cents": response}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("collect_date", collect_date)
    graph.add_node("edit_amount", edit_amount)
    graph.add_edge(START, "collect_date")
    graph.add_edge(START, "edit_amount")
    graph.add_edge("collect_date", END)
    graph.add_edge("edit_amount", END)
    return graph.compile(checkpointer=InMemorySaver())


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    graph = build_graph()
    config = {"configurable": {"thread_id": "parallel-review"}}
    paused = graph.invoke({"claim_id": "CLM-0001"}, config, version="v2")
    responses = {item.id: case["loss_date"] for item in paused.interrupts}
    result = graph.invoke(Command(resume=responses), config, version="v2").value
    return {"prompts": sorted(item.value["kind"] for item in paused.interrupts), "result": result}


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
