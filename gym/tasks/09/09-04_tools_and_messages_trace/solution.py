"""Trace tools and messages: Return a correlated tool error for an unknown policy.. Run this file with Python. No live model or network."""

from langchain_core.messages import AIMessage
from langchain_core.tools import tool
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode

from common.claims import calculate_payout
from common.data import claims_connection
from common.pretty import print_state

DEFAULT_CASE = {"policy_id": "POL-0001", "amount_cents": 125000}


@tool
def lookup_policy(policy_id: str) -> str:
    """Read a fictional policy limit and deductible by exact policy identifier."""
    with claims_connection() as connection:
        row = connection.execute(
            "SELECT limit_cents, deductible_cents FROM policies WHERE policy_id = ?", (policy_id,)
        ).fetchone()
    if row is None:
        raise ValueError("Unknown synthetic policy")
    return f"limit={row['limit_cents']}; deductible={row['deductible_cents']}"


@tool
def proposed_payout(amount_cents: int) -> int:
    """Calculate a proposed synthetic amount; never initiate a payment."""
    return calculate_payout(amount_cents, 200000, 100000)


def build_graph():
    graph = StateGraph(MessagesState)
    graph.add_node("tools", ToolNode([lookup_policy, proposed_payout], handle_tool_errors=False))
    graph.add_edge(START, "tools")
    graph.add_edge("tools", END)
    return graph.compile()


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    calls = [
        {"name": "lookup_policy", "args": {"policy_id": case["policy_id"]}, "id": "policy-call"},
        {
            "name": "proposed_payout",
            "args": {"amount_cents": case["amount_cents"]},
            "id": "payout-call",
        },
    ]
    result = (
        build_graph()
        .invoke({"messages": [AIMessage(content="", tool_calls=calls)]}, version="v2")
        .value
    )
    return {
        "results": sorted(
            [
                {
                    "call_id": message.tool_call_id,
                    "status": message.status,
                    "content": message.content,
                }
                for message in result["messages"]
                if message.type == "tool"
            ],
            key=lambda item: item["call_id"],
        )
    }


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"amount_cents": 125000, "policy_id": "POL-0001"},
        {"amount_cents": 125000, "policy_id": "MISSING"},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Return a correlated tool error for an unknown policy.",
    }


if __name__ == "__main__":
    main()
