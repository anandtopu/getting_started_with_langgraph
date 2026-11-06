"""Reducers combine updates; nodes return only their new evidence. No LLM.

Run: uv run python modules/02_state_and_reducers/examples/02_reducer_findings.py
Expected: receipt remains once, its severity becomes 3, and both checks are logged.
"""

import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {
    "first": {"id": "receipt", "severity": 1},
    "second": {"id": "receipt", "severity": 3},
}


def merge_findings(left: list[dict], right: list[dict]) -> list[dict]:
    indexed = {item["id"]: dict(item) for item in left}
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
    print_state(run())


if __name__ == "__main__":
    main()
