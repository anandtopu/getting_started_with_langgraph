"""Group parallel updates by scope without requiring sibling arrival order. No LLM.

Run: uv run python modules/07_time_travel_and_streaming/examples/03_namespaces_and_errors.py
Expected: a nested document check, a parent identity check, then summary.
"""

import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001"}


class State(TypedDict):
    claim_id: str
    checks: Annotated[list[str], operator.add]
    status: str


def check_document(state: State) -> dict:
    return {"checks": ["document"]}


def check_identity(state: State) -> dict:
    return {"checks": ["identity"]}


def summarize(state: State) -> dict:
    return {"status": "ready" if set(state["checks"]) == {"identity", "document"} else "incomplete"}


def build_graph():
    child = StateGraph(State)
    child.add_node("check_document", check_document)
    child.add_edge(START, "check_document")
    child.add_edge("check_document", END)
    graph = StateGraph(State)
    graph.add_node("document_review", child.compile())
    graph.add_node("check_identity", check_identity)
    graph.add_node("summarize", summarize)
    graph.add_edge(START, "document_review")
    graph.add_edge(START, "check_identity")
    graph.add_edge(["document_review", "check_identity"], "summarize")
    graph.add_edge("summarize", END)
    return graph.compile()


def run(case: dict | None = None) -> dict:
    graph = build_graph()
    events = list(
        graph.stream(
            {**(DEFAULT_CASE if case is None else case), "checks": []},
            stream_mode="updates",
            subgraphs=True,
            version="v2",
        )
    )
    groups: dict[str, list[str]] = {}
    for part in events:
        scope = "/".join(segment.split(":")[0] for segment in part["ns"]) or "parent"
        groups.setdefault(scope, []).extend(part["data"])
    parent_order = [next(iter(part["data"])) for part in events if not part["ns"]]
    return {
        "groups": {key: sorted(value) for key, value in sorted(groups.items())},
        "summary_last": parent_order[-1] == "summarize",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
