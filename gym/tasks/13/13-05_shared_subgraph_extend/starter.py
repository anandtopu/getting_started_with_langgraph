"""Extend shared subgraph: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"amount_cents": 600000, "documents": [], "workflow": "claim"}


def merge_flags(old: list[str], new: list[str]) -> list[str]:
    return sorted(set(old) | set(new))


class State(TypedDict):
    amount_cents: int
    documents: list[str]
    flags: Annotated[list[str], merge_flags]
    workflow: str
    destination: str


def build_fraud_graph():
    def check_amount(state: State) -> dict:
        return {"flags": ["high_value"] if state["amount_cents"] > 500000 else []}

    def check_evidence(state: State) -> dict:
        return {"flags": [] if state["documents"] else ["missing_evidence"]}

    graph = StateGraph(State)
    graph.add_node("check_amount", check_amount)
    graph.add_node("check_evidence", check_evidence)
    graph.add_edge(START, "check_amount")
    graph.add_edge(START, "check_evidence")
    graph.add_edge("check_amount", END)
    graph.add_edge("check_evidence", END)
    return graph.compile()


def build_graph():
    def route(state: State) -> dict:
        if state["workflow"] not in {"claim", "new_policy"}:
            raise ValueError("Unknown workflow")
        risk_flags = set(state["flags"]) - {"intake_checked"}
        return {"destination": state["workflow"] + ("_review" if risk_flags else "_standard")}

    graph = StateGraph(State)
    # KEY IDEA: a compiled graph is a node whose shared keys cross this boundary.
    graph.add_node("fraud_checks", build_fraud_graph())
    graph.add_node("route", route)
    graph.add_edge(START, "fraud_checks")
    graph.add_edge("fraud_checks", "route")
    graph.add_edge("route", END)
    return graph.compile()


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    return (
        build_graph()
        .invoke(
            {**(DEFAULT_CASE if case is None else case), "flags": ["intake_checked"]}, version="v2"
        )
        .value
    )


def run_batch(cases: list[dict]) -> list[dict]:
    return []


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
