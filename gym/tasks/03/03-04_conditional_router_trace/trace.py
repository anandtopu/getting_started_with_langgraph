"""Trace conditional router: Path-map values must match each intended destination.. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"claim_type": "water", "amount_cents": 100000, "missing": []}


class State(TypedDict):
    claim_type: str
    amount_cents: int
    missing: list[str]
    route: str


def route_claim(state: State) -> str:
    amount = state["amount_cents"]
    if type(amount) is not int or amount < 0:
        return "invalid"
    if state["missing"]:
        return "needs_information"
    if (
        state["claim_type"] not in {"water", "theft", "fire", "storm", "liability"}
        or amount > 500000
    ):
        return "specialist"
    return (
        "fast_track"
        if amount <= 100000 and state["claim_type"] in {"water", "theft", "storm"}
        else "standard"
    )


def build_graph():
    builder = StateGraph(State)
    destinations = ["invalid", "needs_information", "specialist", "fast_track", "standard"]
    for destination in destinations:

        def record(state: State, label=destination) -> dict:
            return {"route": label}

        builder.add_node(destination, record)
        builder.add_edge(destination, END)
    builder.add_conditional_edges(
        START, route_claim, {label: "specialist" for label in destinations}
    )
    return builder.compile()


def run(case: dict | None = None) -> dict:
    return build_graph().invoke(dict(DEFAULT_CASE if case is None else case), version="v2").value


def main() -> None:
    try:
        for amount in (100000, 100001, 500001):
            print_state(run({**DEFAULT_CASE, "amount_cents": amount}))
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
