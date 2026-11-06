"""Extend intake nodes: An amount update must not erase the claim identifier.. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "description": "  Pipe burst  ", "amount_cents": "125000"}


class State(TypedDict):
    claim_id: str
    description: str
    amount_cents: int | str
    contact: str


def normalize_description(state: State) -> dict:
    return {"description": state["description"].strip()}


def normalize_amount(state: State) -> dict:
    amount = state["amount_cents"]
    if isinstance(amount, bool):
        raise ValueError("A boolean is not an amount")
    return {"amount_cents": int(amount)}


def normalize_contact(state: State) -> dict:
    return {"contact": str(state.get("contact", "email")).strip().lower()}


def build_graph():
    builder = StateGraph(State)
    builder.add_node("normalize_description", normalize_description)
    builder.add_node("normalize_amount", normalize_amount)
    builder.add_edge(START, "normalize_description")
    builder.add_edge("normalize_description", "normalize_amount")
    builder.add_node("normalize_contact", normalize_contact)
    builder.add_edge("normalize_amount", "normalize_contact")
    builder.add_edge("normalize_contact", END)
    return builder.compile()


def run(case: dict | None = None) -> dict:
    return build_graph().invoke(dict(DEFAULT_CASE if case is None else case), version="v2").value


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
