"""Trace teaching evidence must contain actual node updates, including the failing node."""

import json
from types import SimpleNamespace
from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import interrupt

from common.config import ROOT
from scripts.authoring.traces import capture


def test_trace_captures_node_updates_and_the_first_failed_node():
    class State(TypedDict):
        value: int

    def run(case):
        builder = StateGraph(State)
        builder.add_node("increment", lambda state: {"value": state["value"] + 1})
        builder.add_node("bad_update", lambda state: "not a mapping")
        builder.add_edge(START, "increment")
        builder.add_edge("increment", "bad_update")
        builder.add_edge("bad_update", END)
        return builder.compile().invoke(case, version="v2").value

    evidence = capture(SimpleNamespace(run=run), [{"value": 1}])["cases"][0]
    assert evidence["observed_result"] == {"error": "InvalidUpdateError"}
    assert [row["node"] for row in evidence["node_updates"]] == ["increment", "bad_update"]
    assert evidence["node_updates"][0]["update"] == {"value": 2}
    assert evidence["node_updates"][1]["error_type"] == "InvalidUpdateError"


def test_trace_distinguishes_an_approval_pause_from_a_failure():
    class State(TypedDict):
        value: int

    def run(case):
        builder = StateGraph(State)
        builder.add_node("approval", lambda state: {"value": interrupt("Approve?")})
        builder.add_edge(START, "approval")
        builder.add_edge("approval", END)
        return (
            builder.compile(checkpointer=InMemorySaver())
            .invoke(case, {"configurable": {"thread_id": "trace-pause"}}, version="v2")
            .value
        )

    evidence = capture(SimpleNamespace(run=run), [{"value": 1}])["cases"][0]
    assert len(evidence["node_updates"]) == 1
    assert evidence["node_updates"][0]["paused"] is True
    assert evidence["node_updates"][0]["failed"] is False


def test_published_intake_trace_contains_the_failed_update():
    evidence = json.loads(
        (ROOT / "gym/tasks/01/01-04_intake_nodes_trace/trace.json").read_text("utf-8")
    )
    for case in evidence["cases"]:
        assert case["node_updates"]
        assert case["node_updates"][-1]["failed"] is True
        assert case["node_updates"][-1]["error_type"] == "InvalidUpdateError"
