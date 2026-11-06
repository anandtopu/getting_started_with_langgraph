"""Trace parallel futures: Preserve every parallel graph result.. Run this file with Python. No live model or network."""

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
    findings: Annotated[list[str], lambda old, new: new]


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


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
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
    print_state(run())


def run() -> dict:
    observations = []
    for case in [{"documents": ["estimate", "receipt", "police_report"]}, {"documents": []}]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": "Preserve every parallel graph result."}


if __name__ == "__main__":
    main()
