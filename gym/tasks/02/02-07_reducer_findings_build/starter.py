"""Build reducer findings: A merge must preserve evidence from earlier updates.. Run this file with Python. No live model or network."""

import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {
    "first": {"id": "receipt", "severity": 1},
    "second": {"id": "receipt", "severity": 3},
}


def merge_findings(left: list[dict], right: list[dict]) -> list[dict]:
    indexed = {}
    for finding in right:
        key = finding["id"]
        indexed[key] = {
            "id": key,
            "severity": max(indexed.get(key, {}).get("severity", 0), finding["severity"]),
        }
    return [indexed[key] for key in sorted(indexed)]


class State(TypedDict):
    first: dict
    second: dict
    findings: Annotated[list[dict], merge_findings]
    log: Annotated[list[str], operator.add]
    last: str


def check_estimate(state: State) -> dict:
    return {"findings": [state["first"]], "log": ["estimate"], "last": "estimate"}


def check_receipt(state: State) -> dict:
    return {"findings": [state["second"]], "log": ["receipt"], "last": "receipt"}


def build_graph():
    builder = StateGraph(State)
    builder.add_node("check_estimate", check_estimate)
    builder.add_node("check_receipt", check_receipt)
    builder.add_edge(START, "check_estimate")
    builder.add_edge("check_estimate", "check_receipt")
    builder.add_edge("check_receipt", END)
    return builder.compile()


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    result = (
        build_graph()
        .invoke(
            {**(DEFAULT_CASE if case is None else case), "findings": [], "log": []}, version="v2"
        )
        .value
    )
    return {key: result[key] for key in ("findings", "log", "last")}


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
