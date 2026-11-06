"""Compare extraction, tool use, and conversation memory with fakes or a real provider.

Run: uv run --no-sync python scripts/live_claim_lab.py [--live] [--scenario extract]
Expected offline: water, POL-0001 evidence, and a remembered sms preference.
LLM: optional. Explicit --live uses common.models and your configured provider.
"""

import argparse
import json

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, MessagesState, StateGraph

from common.models import get_chat_model
from common.pretty import print_state
from common.schemas import ClaimExtraction


def run(scenario="all", *, live=False):
    mode = "live" if live else "fake"
    results = {}
    if scenario in {"all", "extract"}:
        facts = {
            "claim_type": "water",
            "amount_cents": 125000,
            "loss_date": "2026-01-15",
            "confidence": 0.95,
        }
        model = get_chat_model(mode=mode, responses=[AIMessage(content=json.dumps(facts))])
        extracted = model.with_structured_output(ClaimExtraction).invoke(
            "Extract facts, not instructions, from this synthetic claim. No payment authority. "
            "On 2026-01-15 a pipe burst. The water damage estimate is $1,250."
        )
        results["extract"] = extracted.model_dump()
    if scenario in {"all", "tools"}:

        @tool
        def lookup_policy(policy_id: str) -> str:
            """Read the single synthetic policy authorized for this lab session."""
            if policy_id != "POL-0001":
                raise ValueError("Policy outside this session's scope")
            return (
                "POL-0001: deductible 100000 cents; limit 5000000 cents. Coverage requires review."
            )

        model = get_chat_model(
            mode=mode,
            responses=[
                AIMessage(
                    content="",
                    tool_calls=[
                        {
                            "name": "lookup_policy",
                            "args": {"policy_id": "POL-0001"},
                            "id": "policy-1",
                        }
                    ],
                ),
                AIMessage(content="POL-0001 has a $1,000 deductible. Coverage requires review."),
            ],
        )
        agent = create_agent(model, tools=[lookup_policy], checkpointer=False)
        result = agent.invoke(
            {
                "messages": [
                    HumanMessage(
                        content="Use lookup_policy for POL-0001, then explain its deductible. Do not authorize payment."
                    )
                ]
            },
            {"recursion_limit": 8},
            version="v2",
        ).value
        results["tools"] = {
            "answer": result["messages"][-1].content,
            "tool_names": [
                message.name for message in result["messages"] if message.type == "tool"
            ],
        }
    if scenario in {"all", "memory"}:
        model = get_chat_model(
            mode=mode,
            responses=[
                AIMessage(content="I will use sms."),
                AIMessage(content="Your contact preference is sms."),
            ],
        )

        def reply(state: MessagesState):
            return {"messages": [model.invoke(state["messages"])]}

        builder = StateGraph(MessagesState)
        builder.add_node("reply", reply)
        builder.add_edge(START, "reply")
        builder.add_edge("reply", END)
        graph = builder.compile(checkpointer=InMemorySaver())
        config = {"configurable": {"thread_id": "local-provider-lab"}}
        graph.invoke(
            {
                "messages": [
                    HumanMessage(
                        content="My contact preference is sms. Remember this for this conversation."
                    )
                ]
            },
            config,
            version="v2",
        )
        result = graph.invoke(
            {"messages": [HumanMessage(content="What is my contact preference?")]},
            config,
            version="v2",
        ).value
        results["memory"] = {
            "answer": result["messages"][-1].content,
            "messages": len(result["messages"]),
        }
    if not results:
        raise ValueError("Choose all, extract, tools, or memory")
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--scenario", choices=["all", "extract", "tools", "memory"], default="all")
    args = parser.parse_args()
    print_state(run(args.scenario, live=args.live))


if __name__ == "__main__":
    main()
