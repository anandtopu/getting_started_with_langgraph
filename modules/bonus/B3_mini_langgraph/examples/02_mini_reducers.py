"""Compare overwrite conflicts and reduced writes with LangGraph. No LLM.

Run: uv run python modules/bonus/B3_mini_langgraph/examples/02_mini_reducers.py
Expected: parallel overwrite fails in both engines; a reducer retains both findings.
"""

import operator
from typing import Annotated, TypedDict

from langgraph.errors import InvalidUpdateError
from langgraph.graph import END, START, StateGraph

from common.mini_graph import MiniGraph, WriteConflict
from common.pretty import print_state

DEFAULT_CASE = {"use_reducer": True}


class Reduced(TypedDict):
    findings: Annotated[list[str], operator.add]


class Overwrite(TypedDict):
    findings: list[str]


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    mini = MiniGraph(
        {
            "policy": lambda state, resume: {"findings": ["policy"]},
            "estimate": lambda state, resume: {"findings": ["estimate"]},
        },
        {},
        ["policy", "estimate"],
        {"findings": operator.add} if case["use_reducer"] else {},
    )
    graph = StateGraph(Reduced if case["use_reducer"] else Overwrite)
    for name in ("policy", "estimate"):
        graph.add_node(name, lambda state, name=name: {"findings": [name]})
        graph.add_edge(START, name)
        graph.add_edge(name, END)
    observed = {}
    for name, call in {
        "mini": lambda: mini.run({"findings": []}).values,
        "langgraph": lambda: graph.compile().invoke({"findings": []}, version="v2").value,
    }.items():
        try:
            observed[name] = {"findings": sorted(call()["findings"])}
        except (WriteConflict, InvalidUpdateError):
            observed[name] = {"conflict": True}
    return {**observed, "equal": observed["mini"] == observed["langgraph"]}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
