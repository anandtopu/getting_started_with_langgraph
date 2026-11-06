"""Version 08: durable estimate waits followed by the complete specialist workflow."""

from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from langgraph.store.memory import InMemoryStore
from langgraph.types import Command, interrupt

from common.copilot import v06, v07
from common.data import load_submission


class DurableClaimState(v07.TeamState):
    requested_on: str
    received_on: str
    waited_days: int


def await_estimate(state: DurableClaimState) -> dict:
    response = interrupt(
        {
            "kind": "estimate_wait",
            "claim_id": state["claim"]["claim_id"],
            "requested_on": state["requested_on"],
        }
    )
    if (
        not isinstance(response, dict)
        or not isinstance(response.get("document_id"), str)
        or not response["document_id"].strip()
        or not isinstance(response.get("received_on"), str)
    ):
        raise ValueError("Resume with document_id and received_on")
    elapsed = (
        date.fromisoformat(response["received_on"]) - date.fromisoformat(state["requested_on"])
    ).days
    if elapsed < 0:
        raise ValueError("Estimate receipt precedes its request")
    claim = {
        **state["claim"],
        "documents": sorted(set(state["claim"].get("documents", []) + [response["document_id"]])),
    }
    return {
        "claim": claim,
        "received_on": response["received_on"],
        "waited_days": elapsed,
        "audit": ["estimate_received"],
    }


def build_graph(checkpointer=None, store=None):
    graph = StateGraph(DurableClaimState, context_schema=v06.CustomerContext)
    graph.add_node("await_estimate", await_estimate)
    graph.add_node("review_claim", v07.build_graph(checkpointer=True, store=store))
    graph.add_edge(START, "await_estimate")
    graph.add_edge("await_estimate", "review_claim")
    graph.add_edge("review_claim", END)
    return graph.compile(
        checkpointer=checkpointer if checkpointer is not None else InMemorySaver(),
        store=store if store is not None else InMemoryStore(),
    )


def run(claim=None, *, approved=True, received_on="2026-01-04"):
    claim = load_submission(1) if claim is None else claim
    config = {"configurable": {"thread_id": claim["claim_id"]}}
    context = v06.CustomerContext(claim["customer_id"])
    with TemporaryDirectory(prefix="larkspur-copilot-") as directory:
        path = str(Path(directory) / "claims.db")
        with SqliteSaver.from_conn_string(path) as saver:
            build_graph(saver).invoke(
                {"claim": claim, "audit": [], "findings": [], "requested_on": "2026-01-01"},
                config,
                context=context,
                version="v2",
            )
        with SqliteSaver.from_conn_string(path) as saver:
            graph = build_graph(saver)
            result = graph.invoke(
                Command(resume={"document_id": "DOC-ESTIMATE", "received_on": received_on}),
                config,
                context=context,
                version="v2",
            )
            if result.interrupts:
                result = graph.invoke(
                    Command(resume={"approved": approved}), config, context=context, version="v2"
                )
            return result.value
