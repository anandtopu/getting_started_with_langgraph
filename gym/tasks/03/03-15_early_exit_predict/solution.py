"""Predict early exit across the declared cases. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "amount_cents": 0, "duplicate_of": None}


class State(TypedDict):
    claim_id: str
    amount_cents: int
    duplicate_of: str | None
    reason: str
    assigned: bool


def screen(state: State) -> dict:
    amount = state["amount_cents"]
    reason = (
        "duplicate"
        if state["duplicate_of"]
        else "invalid"
        if type(amount) is not int or amount < 0
        else "eligible"
    )
    return {"reason": reason, "assigned": False}


def next_step(state: State) -> str:
    return "assign" if state["reason"] == "eligible" else END


def assign(state: State) -> dict:
    return {"assigned": True}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("screen", screen)
    graph.add_node("assign", assign)
    graph.add_edge(START, "screen")
    graph.add_conditional_edges("screen", next_step, {"assign": "assign", END: END})
    graph.add_edge("assign", END)
    return graph.compile()


def scenario(case: dict | None = None) -> dict:
    return build_graph().invoke(dict(DEFAULT_CASE if case is None else case), version="v2").value


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"amount_cents": 0, "claim_id": "CLM-0001", "duplicate_of": None},
        {"amount_cents": -1, "claim_id": "CLM-0001", "duplicate_of": None},
        {"amount_cents": True, "claim_id": "CLM-0001", "duplicate_of": None},
        {"amount_cents": 0, "claim_id": "CLM-0001", "duplicate_of": "CLM-0021"},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
