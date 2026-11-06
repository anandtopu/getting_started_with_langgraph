"""Probe the installed LangGraph interfaces used by the foundation."""

import operator
from typing import Annotated, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, GraphOutput, interrupt
from pydantic import BaseModel

from scripts.first_graph import build_graph


def test_first_graph_value_and_mermaid():
    output = build_graph().invoke({"claim": {"claim_id": "CLM-1"}, "steps": []}, version="v2")
    assert isinstance(output, GraphOutput)
    assert output.value["status"] == "needs_information"
    assert output.value["steps"] == ["normalize_claim", "check_required_fields", "route_claim"]
    assert not output.interrupts
    assert "check_required_fields" in build_graph().get_graph().draw_mermaid()


def test_interrupt_and_checkpoint_contract():
    class State(TypedDict):
        claim_id: str
        approved: bool

    def approve(state):
        return {
            "approved": bool(interrupt({"claim_id": state["claim_id"], "amount_cents": 600_000}))
        }

    builder = StateGraph(State)
    builder.add_node("approve", approve)
    builder.add_edge(START, "approve")
    builder.add_edge("approve", END)
    graph = builder.compile(checkpointer=InMemorySaver())
    config = {"configurable": {"thread_id": "contract-test"}}
    pending = graph.invoke({"claim_id": "CLM-1", "approved": False}, config, version="v2")
    assert pending.interrupts[0].value["amount_cents"] == 600_000
    completed = graph.invoke(Command(resume=True), config, version="v2")
    assert completed.value["approved"] and not completed.interrupts
    assert graph.get_state(config).values["approved"]
    assert len(list(graph.get_state_history(config))) >= 3


def test_parallel_reducer_and_stream_part_contract():
    class State(TypedDict):
        findings: Annotated[list[str], operator.add]

    builder = StateGraph(State)
    builder.add_node("check_estimate", lambda state: {"findings": ["estimate"]})
    builder.add_node("check_receipt", lambda state: {"findings": ["receipt"]})
    for name in ("check_estimate", "check_receipt"):
        builder.add_edge(START, name)
        builder.add_edge(name, END)
    graph = builder.compile()
    parts = list(graph.stream({"findings": []}, stream_mode=["values", "updates"], version="v2"))
    assert all({"type", "ns", "data"} <= part.keys() for part in parts)
    values = [part for part in parts if part["type"] == "values"]
    assert sorted(values[-1]["data"]["findings"]) == ["estimate", "receipt"]


def test_pydantic_v2_output_is_coerced():
    class Output(BaseModel):
        status: str = "received"

    builder = StateGraph(Output)
    builder.add_node("validate_claim", lambda state: {"status": "validated"})
    builder.add_edge(START, "validate_claim")
    builder.add_edge("validate_claim", END)
    assert isinstance(builder.compile().invoke({}, version="v2").value, Output)
