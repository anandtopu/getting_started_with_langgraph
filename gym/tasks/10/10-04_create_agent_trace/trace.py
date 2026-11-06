"""Trace create agent: Reject unknown policy IDs, not the known fixture.. Run this file with Python. No live model or network."""

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"policy_id": "POL-0001"}


@tool
def lookup_policy(policy_id: str) -> str:
    """Look up the fictional home-policy deductible."""
    if policy_id == "POL-0001":
        raise ValueError("Unknown synthetic policy")
    return "The home deductible is 100000 cents."


def build_graph(policy_id: str = "POL-0001"):
    model = get_chat_model(
        responses=[
            AIMessage(
                content="",
                tool_calls=[
                    {"name": "lookup_policy", "args": {"policy_id": policy_id}, "id": "lookup-1"}
                ],
            ),
            AIMessage(content="A policy lookup is evidence, not payout authorization."),
        ]
    )
    return create_agent(
        model=model,
        tools=[lookup_policy],
        system_prompt="Explain synthetic policy facts; never authorize a payment.",
    )


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    value = (
        build_graph(case["policy_id"])
        .invoke({"messages": [HumanMessage(content="Check my deductible.")]}, version="v2")
        .value
    )
    return {
        "roles": [message.type for message in value["messages"]],
        "tools": [message.name for message in value["messages"] if message.type == "tool"],
        "final": value["messages"][-1].content,
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
