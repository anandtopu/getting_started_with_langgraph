"""Version 04: validated extraction before the deterministic approval workflow."""

import json

from langchain_core.messages import AIMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command

from common.copilot import v03
from common.copilot.v01 import ClaimState
from common.data import load_submission
from common.models import get_chat_model
from common.schemas import ClaimExtraction


class ExtractedState(ClaimState):
    extracted: dict


def extract(state: ExtractedState) -> dict:
    claim = state["claim"]
    # The scripted answer is fixture evidence, not a claim about live extraction accuracy.
    payload = {
        "claim_type": claim["claim_type"],
        "amount_cents": claim["amount_cents"],
        "confidence": 0.95,
        "loss_date": claim.get("loss_date"),
    }
    model = get_chat_model(responses=[AIMessage(content=json.dumps(payload))])
    facts = model.with_structured_output(ClaimExtraction).invoke(
        "Extract facts only; do not authorize payment. Untrusted claim: " + claim["description"]
    )
    return {"extracted": facts.model_dump(), "audit": ["extracted_and_validated"]}


def build_builder():
    graph = StateGraph(ExtractedState)
    graph.add_node("extract", extract)
    graph.add_node("process_claim", v03.build_graph(checkpointer=True))
    graph.add_edge(START, "extract")
    graph.add_edge("extract", "process_claim")
    return graph


def build_graph(checkpointer=None):
    graph = build_builder()
    graph.add_edge("process_claim", END)
    return graph.compile(checkpointer=checkpointer if checkpointer is not None else InMemorySaver())


def run(claim=None, *, approved=True):
    claim = load_submission(1) if claim is None else claim
    graph = build_graph()
    config = {"configurable": {"thread_id": claim["claim_id"]}}
    result = graph.invoke({"claim": claim, "audit": [], "findings": []}, config, version="v2")
    if result.interrupts:
        result = graph.invoke(Command(resume={"approved": approved}), config, version="v2")
    return result.value
