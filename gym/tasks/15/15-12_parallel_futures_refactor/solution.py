"""Refactor parallel futures: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

import operator
from typing import Annotated, TypedDict

from langgraph.func import entrypoint, task
from langgraph.graph import END, START, StateGraph
from langgraph.types import Send

from common.pretty import print_state

DEFAULT_CASE = {"documents": ["estimate", "receipt", "police_report"]}


def finding(document: str) -> str:
    return document + (":review" if document == "police_report" else ":ready")


@task
def inspect_document(document: str) -> str:
    return finding(document)


@entrypoint()
def functional(documents: list[str]) -> list[str]:
    futures = [inspect_document(document) for document in documents]
    return sorted(future.result() for future in futures)


class State(TypedDict):
    documents: list[str]
    findings: Annotated[list[str], operator.add]


class Worker(TypedDict):
    document: str


def build_graph():
    graph = StateGraph(State)
    graph.add_node(
        "inspect_document",
        lambda state: {"findings": [finding(state["document"])]},
        input_schema=Worker,
    )
    graph.add_conditional_edges(
        START,
        lambda state: (
            [Send("inspect_document", {"document": document}) for document in state["documents"]]
            or [END]
        ),
        ["inspect_document", END],
    )
    graph.add_edge("inspect_document", END)
    return graph.compile()


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
    first = functional.invoke(case["documents"], version="v2").value
    second = (
        build_graph().invoke({"documents": case["documents"], "findings": []}, version="v2").value
    )
    return {
        "functional": first,
        "graph": sorted(second["findings"]),
        "equal": first == sorted(second["findings"]),
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
