"""Version 05: a read-only policy agent inside the approved business workflow."""

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command

from common.claims import calculate_payout as payout_rule
from common.copilot import v04
from common.data import claims_connection, load_submission
from common.models import get_chat_model


class AgentClaimState(v04.ExtractedState):
    policy_evidence: list[dict]
    agent_explanation: str


def policy_agent(state: AgentClaimState) -> dict:
    if state["route"] in {"needs_information", "invalid", "duplicate"}:
        return {
            "policy_evidence": [],
            "agent_explanation": "Intake requires correction or duplicate review before policy analysis.",
            "audit": ["policy_analysis_deferred"],
        }
    claim = state["claim"]
    with claims_connection() as connection:
        row = connection.execute(
            "SELECT * FROM policies WHERE policy_id = ?", (claim["policy_id"],)
        ).fetchone()
        if row is None or row["customer_id"] != claim["customer_id"]:
            raise ValueError("Policy must belong to the claim customer")
        policy = dict(row)

    @tool
    def lookup_policy() -> dict:
        """Read only this claim's policy limit and deductible."""
        return {key: policy[key] for key in ("policy_id", "limit_cents", "deductible_cents")}

    @tool
    def get_claim_history() -> list[dict]:
        """Read synthetic prior claim identifiers for this customer only."""
        with claims_connection() as connection:
            rows = connection.execute(
                "SELECT claim_id, route FROM claims WHERE customer_id = ? ORDER BY claim_id",
                (claim["customer_id"],),
            ).fetchall()
        return [dict(row) for row in rows]

    @tool
    def check_coverage() -> dict:
        """Check the fixture's covered claim types; missing policy evidence requires review."""
        return {
            "claim_type": claim["claim_type"],
            "requires_policy_review": True,
            "note": "A deductible calculation alone does not establish coverage.",
        }

    @tool
    def calculate_payout() -> int:
        """Propose cents within this policy's limit; never make a payment."""
        return payout_rule(claim["amount_cents"], policy["limit_cents"], policy["deductible_cents"])

    tools = [lookup_policy, get_claim_history, check_coverage, calculate_payout]
    calls = [
        {"name": item.name, "args": {}, "id": "evidence-" + str(i)} for i, item in enumerate(tools)
    ]
    agent = create_agent(
        model=get_chat_model(
            responses=[
                AIMessage(content="", tool_calls=calls),
                AIMessage(
                    content="Policy evidence collected. An authorized adjuster must confirm coverage."
                ),
            ]
        ),
        tools=tools,
        checkpointer=False,
    )
    result = agent.invoke(
        {"messages": [HumanMessage(content="Collect policy evidence for this claim.")]},
        {"recursion_limit": 12},
        version="v2",
    ).value
    return {
        "policy_evidence": [
            {"tool": message.name, "result": message.content}
            for message in result["messages"]
            if message.type == "tool"
        ],
        "agent_explanation": result["messages"][-1].content,
        "audit": ["policy_evidence_collected"],
    }


def build_builder():
    graph = StateGraph(AgentClaimState)
    graph.add_node("intake", v04.build_graph(checkpointer=True))
    graph.add_node("policy_agent", policy_agent)
    graph.add_edge(START, "intake")
    graph.add_edge("intake", "policy_agent")
    return graph


def build_graph(checkpointer=None):
    graph = build_builder()
    graph.add_edge("policy_agent", END)
    return graph.compile(checkpointer=checkpointer if checkpointer is not None else InMemorySaver())


def run(claim=None, *, approved=True):
    claim = load_submission(1) if claim is None else claim
    graph = build_graph()
    config = {"configurable": {"thread_id": claim["claim_id"]}}
    result = graph.invoke({"claim": claim, "audit": [], "findings": []}, config, version="v2")
    if result.interrupts:
        result = graph.invoke(Command(resume={"approved": approved}), config, version="v2")
    return result.value
