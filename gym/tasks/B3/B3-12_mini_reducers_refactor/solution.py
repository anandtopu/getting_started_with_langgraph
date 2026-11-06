"""Refactor mini reducers: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

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


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
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
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
