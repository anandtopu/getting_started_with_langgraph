"""Version 02: parallel document evidence and checkpointed claim sessions."""

from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Send

from common.copilot.v01 import ClaimState, normalize, route, validate
from common.data import load_submission


class DocumentState(TypedDict):
    document_id: str


def dispatch_documents(state: ClaimState) -> list:
    documents = state["claim"].get("documents", [])
    return [Send("review_document", {"document_id": item}) for item in documents] or ["route"]


def review_document(state: DocumentState) -> dict:
    return {"findings": ["reviewed:" + state["document_id"]]}


def build_builder():
    graph = StateGraph(ClaimState)
    graph.add_node("normalize", normalize)
    graph.add_node("validate", validate)
    graph.add_node("review_document", review_document, input_schema=DocumentState)
    graph.add_node("route", route, defer=True)
    graph.add_edge(START, "normalize")
    graph.add_edge("normalize", "validate")
    graph.add_conditional_edges("validate", dispatch_documents, ["review_document", "route"])
    graph.add_edge("review_document", "route")
    return graph


def build_graph(checkpointer=None):
    graph = build_builder()
    graph.add_edge("route", END)
    return graph.compile(checkpointer=checkpointer if checkpointer is not None else InMemorySaver())


def run(claim: dict | None = None) -> dict:
    payload = load_submission(1) if claim is None else claim
    return (
        build_graph()
        .invoke(
            {"claim": payload, "audit": [], "findings": []},
            {"configurable": {"thread_id": payload["claim_id"]}},
            version="v2",
        )
        .value
    )
