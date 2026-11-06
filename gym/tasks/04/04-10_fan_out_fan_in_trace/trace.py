"""Diagnose fan out fan in from execution evidence. Run this file with Python. No live model or network."""

import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import Send

from common.pretty import print_state

DEFAULT_CASE = {
    "documents": [{"id": "DOC-001", "kind": "estimate"}, {"id": "DOC-021", "kind": "police"}]
}


class State(TypedDict):
    documents: list[dict]
    pending_police: Annotated[list[dict], operator.add]
    findings: list[str]
    summaries: Annotated[list[list[str]], operator.add]


class Worker(TypedDict):
    document: dict


def dispatch(state: State) -> list:
    return [
        Send("prepare_police" if doc["kind"] == "police" else "review_document", {"document": doc})
        for doc in state["documents"]
    ] or ["summarize"]


def review_document(state: Worker) -> dict:
    return {"findings": [state["document"]["id"]]}


def prepare_police(state: Worker) -> dict:
    return {"pending_police": [state["document"]]}


def review_police(state: State) -> dict:
    return {"findings": [doc["id"] for doc in state["pending_police"]]}


def summarize(state: State) -> dict:
    return {"summaries": [sorted(state["findings"])]}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("review_document", review_document, input_schema=Worker)
    graph.add_node("prepare_police", prepare_police, input_schema=Worker)
    graph.add_node("review_police", review_police)
    graph.add_node("summarize", summarize, defer=True)
    graph.add_conditional_edges(START, dispatch, ["review_document", "prepare_police", "summarize"])
    graph.add_edge("prepare_police", "review_police")
    graph.add_edge("review_document", "summarize")
    graph.add_edge("review_police", "summarize")
    graph.add_edge("summarize", END)
    return graph.compile()


def run(case: dict | None = None) -> dict:
    result = (
        build_graph()
        .invoke(
            {
                **(DEFAULT_CASE if case is None else case),
                "pending_police": [],
                "findings": [],
                "summaries": [],
            },
            version="v2",
        )
        .value
    )
    return {"findings": sorted(result["findings"]), "summaries": result["summaries"]}


def main() -> None:
    try:
        print_state(run())
        print(build_graph().get_graph().draw_mermaid())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
