"""Version 06: customer memory and a bounded decision-letter review."""

from dataclasses import dataclass

from langchain_core.messages import AIMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.runtime import Runtime
from langgraph.store.memory import InMemoryStore
from langgraph.types import Command

from common.copilot import v05
from common.data import load_submission
from common.models import get_chat_model


@dataclass
class CustomerContext:
    customer_id: str


class MemoryClaimState(v05.AgentClaimState):
    preference: str
    letter: str
    letter_accepted: bool
    letter_attempts: int


def remember(state: MemoryClaimState, runtime: Runtime[CustomerContext]) -> dict:
    if runtime.context.customer_id != state["claim"]["customer_id"]:
        raise PermissionError("Customer context does not own this claim")
    namespace = ("customers", runtime.context.customer_id, "semantic")
    item = runtime.store.get(namespace, "contact")
    preference = item.value["preference"] if item else "email"
    runtime.store.put(
        ("customers", runtime.context.customer_id, "episodic"),
        state["claim"]["claim_id"],
        {"route": state["route"]},
    )
    return {"preference": preference, "audit": ["customer_memory_read"]}


def draft_letter(state: MemoryClaimState) -> dict:
    # The deterministic expected phrase makes this review reproducible, not production-ready.
    decision = "review completed" if state["approved"] else "not approved"
    responses = [
        AIMessage(content="Claim processed."),
        AIMessage(content=f"Thank you. Your claim is {decision}. No payment has been issued."),
    ]
    model = get_chat_model(responses=responses)
    accepted, text, attempts = False, "", 0
    while not accepted and attempts < 2:
        text = model.invoke(f"Use a respectful tone and the exact decision: {decision}.").content
        attempts += 1
        accepted = "Thank you" in text and decision in text and "No payment" in text
    return {
        "letter": text,
        "letter_accepted": accepted,
        "letter_attempts": attempts,
        "audit": ["letter_reviewed"],
    }


def build_graph(checkpointer=None, store=None):
    def authorize_customer(state: MemoryClaimState, runtime: Runtime[CustomerContext]) -> dict:
        if runtime.context.customer_id != state["claim"]["customer_id"]:
            raise PermissionError("Customer context does not own this claim")
        return {}

    graph = StateGraph(MemoryClaimState, context_schema=CustomerContext)
    graph.add_node("authorize_customer", authorize_customer)
    graph.add_node("intake_and_evidence", v05.build_graph(checkpointer=True))
    graph.add_node("remember", remember)
    graph.add_node("draft_letter", draft_letter)
    graph.add_edge(START, "authorize_customer")
    graph.add_edge("authorize_customer", "intake_and_evidence")
    graph.add_edge("intake_and_evidence", "remember")
    graph.add_edge("remember", "draft_letter")
    graph.add_edge("draft_letter", END)
    return graph.compile(
        checkpointer=checkpointer if checkpointer is not None else InMemorySaver(),
        store=store if store is not None else InMemoryStore(),
    )


def run(claim=None, *, approved=True, preference="email"):
    claim = load_submission(1) if claim is None else claim
    store = InMemoryStore()
    store.put(
        ("customers", claim["customer_id"], "semantic"), "contact", {"preference": preference}
    )
    graph = build_graph(store=store)
    config = {"configurable": {"thread_id": claim["claim_id"]}}
    context = CustomerContext(claim["customer_id"])
    result = graph.invoke(
        {"claim": claim, "audit": [], "findings": []}, config, context=context, version="v2"
    )
    if result.interrupts:
        result = graph.invoke(
            Command(resume={"approved": approved}), config, context=context, version="v2"
        )
    return result.value
