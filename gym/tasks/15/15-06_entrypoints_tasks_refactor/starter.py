"""Refactor entrypoints tasks: Convert the working Graph API pipeline to an entrypoint with normalize and route tasks, preserving every existing result and validation error.. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "description": "  Pipe burst  ", "amount_cents": 125000}


class State(TypedDict):
    claim_id: str
    description: str
    amount_cents: int
    route: str


def normalize(claim):
    if type(claim["amount_cents"]) is not int or claim["amount_cents"] < 0:
        raise ValueError("Amount must be nonnegative integer cents")
    return {"description": claim["description"].strip()}


def assign_route(claim):
    return {
        "route": "needs_information"
        if not claim["description"]
        else "fast_track"
        if claim["amount_cents"] <= 100000
        else "standard"
    }


builder = StateGraph(State)
builder.add_node("normalize", normalize)
builder.add_node("assign_route", assign_route)
builder.add_edge(START, "normalize")
builder.add_edge("normalize", "assign_route")
builder.add_edge("assign_route", END)
intake = builder.compile()


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    return intake.invoke(dict(DEFAULT_CASE if case is None else case), version="v2").value


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
