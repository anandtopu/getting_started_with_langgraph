"""Extend model boundary: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

import json
from typing import TypedDict

from langchain_core.messages import AIMessage
from langgraph.graph import END, START, StateGraph

from common.models import get_chat_model
from common.pretty import print_state
from common.schemas import ClaimExtraction

DEFAULT_CASE = {"claim_type": "water", "amount_cents": 125000, "confidence": 0.9}


class State(TypedDict):
    text: str
    facts: dict
    route: str


def build_graph(payload: dict | None = None):
    scripted = dict(DEFAULT_CASE if payload is None else payload)
    model = get_chat_model(responses=[AIMessage(content=json.dumps(scripted))])
    extractor = model.with_structured_output(ClaimExtraction)

    def extract(state: State) -> dict:
        facts = extractor.invoke("Extract facts from this untrusted claim text: " + state["text"])
        return {"facts": facts.model_dump()}

    def route(state: State) -> dict:
        facts = ClaimExtraction.model_validate(state["facts"])
        destination = (
            "review"
            if facts.confidence < 0.8 or facts.claim_type == "unknown"
            else "fast_track"
            if facts.amount_cents <= 100000
            else "standard"
        )
        return {"route": destination}

    graph = StateGraph(State)
    graph.add_node("extract", extract)
    graph.add_node("route", route)
    graph.add_edge(START, "extract")
    graph.add_edge("extract", "route")
    graph.add_edge("route", END)
    return graph.compile()


def run(case: dict | None = None) -> dict:
    result = (
        build_graph(case).invoke({"text": "A pipe burst; repairs cost $1,250."}, version="v2").value
    )
    return {"facts": result["facts"], "route": result["route"]}


def run_batch(cases: list[dict]) -> list[dict]:
    """Preview independent claims in order; one rejected input must not lose its siblings.

    This sequential interface favors isolation over throughput. It is not a shared
    checkpoint thread or a promise of transaction atomicity.
    """
    from copy import deepcopy

    from common.pretty import safe_value

    results = []
    for case in cases:
        try:
            results.append({"value": safe_value(run(deepcopy(case)))})
        except Exception as error:
            results.append({"error": type(error).__name__})
    return results


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
