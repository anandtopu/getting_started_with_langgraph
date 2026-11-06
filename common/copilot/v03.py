"""Version 03: persisted human approval and resumable high-value review."""

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END
from langgraph.types import Command, interrupt

from common.copilot.v01 import ClaimState
from common.copilot.v02 import build_builder
from common.data import load_submission


def approve_claim(state: ClaimState) -> dict:
    if state["route"] in {"needs_information", "duplicate", "invalid"}:
        return {"approved": False, "approval_reason": state["route"]}
    if state["claim"]["amount_cents"] <= 500000 and state["route"] in {"fast_track", "standard"}:
        return {"approved": True, "approval_reason": "within_synthetic_auto_limit"}
    response = interrupt(
        {
            "kind": "payout_approval",
            "claim_id": state["claim"]["claim_id"],
            "amount_cents": state["claim"]["amount_cents"],
        }
    )
    if not isinstance(response, dict) or type(response.get("approved")) is not bool:
        raise ValueError("Provide an explicit boolean approval")
    return {
        "approved": response["approved"],
        "approval_reason": "human_approved" if response["approved"] else "human_rejected",
    }


def build_graph(checkpointer=None):
    graph = build_builder()
    graph.add_node("approve_claim", approve_claim)
    graph.add_edge("route", "approve_claim")
    graph.add_edge("approve_claim", END)
    return graph.compile(checkpointer=checkpointer if checkpointer is not None else InMemorySaver())


def run(claim: dict | None = None, *, approved: bool = True) -> dict:
    payload = load_submission(1) if claim is None else claim
    graph = build_graph()
    config = {"configurable": {"thread_id": payload["claim_id"]}}
    result = graph.invoke({"claim": payload, "audit": [], "findings": []}, config, version="v2")
    if result.interrupts:
        result = graph.invoke(Command(resume={"approved": approved}), config, version="v2")
    return result.value
