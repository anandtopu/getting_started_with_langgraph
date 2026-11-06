"""Version 10: trusted authorization, bound human approval, and idempotent effects."""

from dataclasses import dataclass
from typing import Any

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.runtime import Runtime
from langgraph.store.memory import InMemoryStore
from langgraph.types import interrupt

from common.claims import calculate_payout
from common.copilot import v06, v09
from common.data import claims_connection


@dataclass
class AuthorizedContext(v06.CustomerContext):
    principal_id: str
    role: str
    ledger: Any


class SecureClaimState(v09.StreamingClaimState):
    payment_status: str
    proposed_cents: int
    effect_created: bool


def authorize_intake(state: SecureClaimState, runtime: Runtime[AuthorizedContext]) -> dict:
    if runtime.context.customer_id != state["claim"]["customer_id"]:
        raise PermissionError("Authenticated customer does not own this claim")
    return {"audit": ["ownership_verified"]}


def approve_payment(state: SecureClaimState, runtime: Runtime[AuthorizedContext]) -> dict:
    if not state["approved"]:
        return {"payment_status": "not_approved", "proposed_cents": 0, "effect_created": False}
    claim = state["claim"]
    with claims_connection() as connection:
        policy = connection.execute(
            "SELECT * FROM policies WHERE policy_id = ? AND customer_id = ?",
            (claim["policy_id"], runtime.context.customer_id),
        ).fetchone()
    if policy is None:
        raise PermissionError("Policy ownership could not be verified")
    amount = calculate_payout(
        claim["amount_cents"], policy["limit_cents"], policy["deductible_cents"]
    )
    response = interrupt(
        {
            "kind": "payment_approval",
            "claim_id": claim["claim_id"],
            "amount_cents": amount,
            "requires": "adjuster approval and coverage confirmation",
        }
    )
    if runtime.context.role != "adjuster":
        raise PermissionError("Only an authenticated adjuster may decide payment")
    if not isinstance(response, dict) or type(response.get("approved")) is not bool:
        raise ValueError("An explicit boolean approval is required")
    if not response["approved"]:
        return {"payment_status": "rejected", "proposed_cents": amount, "effect_created": False}
    if response.get("coverage_confirmed") is not True:
        raise ValueError("The adjuster must confirm policy coverage")
    # KEY IDEA: amount and identity come from trusted state, never from the model or resume payload.
    created = runtime.context.ledger.record(
        "payment:" + claim["claim_id"],
        {"claim_id": claim["claim_id"], "amount_cents": amount, "kind": "synthetic_payment"},
    )
    return {
        "payment_status": "recorded",
        "proposed_cents": amount,
        "effect_created": created,
        "audit": ["payment_authorized_and_recorded"],
    }


def build_builder(store=None):
    graph = StateGraph(SecureClaimState, context_schema=AuthorizedContext)
    graph.add_node("authorize_intake", authorize_intake)
    graph.add_node("review", v09.build_graph(checkpointer=True, store=store))
    graph.add_node("approve_payment", approve_payment)
    graph.add_edge(START, "authorize_intake")
    graph.add_edge("authorize_intake", "review")
    graph.add_edge("review", "approve_payment")
    return graph


def build_graph(checkpointer=None, store=None):
    graph = build_builder(store)
    graph.add_edge("approve_payment", END)
    return graph.compile(
        checkpointer=checkpointer if checkpointer is not None else InMemorySaver(),
        store=store if store is not None else InMemoryStore(),
    )
