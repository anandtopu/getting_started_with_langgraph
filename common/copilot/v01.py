"""Version 01: normalized intake, explicit routing, and accumulated audit evidence."""

from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph

from common.claims import missing_fields, normalize_claim, route_claim
from common.data import load_submission


def merge_milestones(old: list[str], new: list[str]) -> list[str]:
    """Deduplicate named milestones returned through shared parent/child channels.

    These labels summarize progress; they are not an immutable event audit log.
    Production event records need their own unique event IDs and durable sink.
    """
    return list(dict.fromkeys([*old, *new]))


def merge_findings(old: list[str], new: list[str]) -> list[str]:
    return sorted(set(old) | set(new))


class ClaimState(TypedDict):
    claim: dict
    missing: list[str]
    route: str
    audit: Annotated[list[str], merge_milestones]
    findings: Annotated[list[str], merge_findings]
    approved: bool
    approval_reason: str


def normalize(state: ClaimState) -> dict:
    return {"claim": normalize_claim(state["claim"]), "audit": ["normalized"]}


def validate(state: ClaimState) -> dict:
    missing = missing_fields(state["claim"])
    return {
        "missing": missing,
        "findings": ["missing:" + key for key in missing],
        "audit": ["validated"],
    }


def route(state: ClaimState) -> dict:
    return {"route": route_claim(state["claim"]), "audit": ["routed"]}


def build_graph():
    graph = StateGraph(ClaimState)
    graph.add_node("normalize", normalize)
    graph.add_node("validate", validate)
    graph.add_node("route", route)
    graph.add_edge(START, "normalize")
    graph.add_edge("normalize", "validate")
    graph.add_edge("validate", "route")
    graph.add_edge("route", END)
    return graph.compile()


def run(claim: dict | None = None) -> dict:
    payload = load_submission(1) if claim is None else claim
    return build_graph().invoke({"claim": payload, "audit": [], "findings": []}, version="v2").value
