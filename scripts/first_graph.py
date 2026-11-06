"""Run a deterministic three-step Larkspur intake graph.

Concepts: TypedDict, partial updates, nodes, edges, and v2 invocation.
Run: uv run python scripts/first_graph.py
Expected: status ready; steps normalize_claim, check_required_fields, route_claim.
LLM: none. Cost: $0. Uses synthetic data only.
"""

import operator
from typing import Annotated, Any, TypedDict

from langgraph.graph import END, START, StateGraph

from common.claims import checklist, missing_fields, normalize_claim
from common.gym_fixtures import checklist_cases
from common.pretty import print_state


class IntakeState(TypedDict, total=False):
    claim: dict[str, Any]
    missing: list[str]
    status: str
    steps: Annotated[list[str], operator.add]


def normalize(state: IntakeState) -> dict[str, Any]:
    return {"claim": normalize_claim(state["claim"]), "steps": ["normalize_claim"]}


def validate(state: IntakeState) -> dict[str, Any]:
    return {"missing": missing_fields(state["claim"]), "steps": ["check_required_fields"]}


def route(state: IntakeState) -> dict[str, Any]:
    return {"status": checklist(state["claim"])["status"], "steps": ["route_claim"]}


def build_graph() -> Any:
    builder = StateGraph(IntakeState)
    builder.add_node("normalize_claim", normalize)
    builder.add_node("check_required_fields", validate)
    builder.add_node("route_claim", route)
    builder.add_edge(START, "normalize_claim")
    builder.add_edge("normalize_claim", "check_required_fields")
    builder.add_edge("check_required_fields", "route_claim")
    builder.add_edge("route_claim", END)
    return builder.compile()


def main() -> None:
    graph = build_graph()
    # KEY IDEA: v2 separates the graph's output value from pending human interrupts.
    result = graph.invoke({"claim": checklist_cases()[0], "steps": []}, version="v2")
    print_state(result.value)
    print(graph.get_graph().draw_mermaid())


if __name__ == "__main__":
    main()
