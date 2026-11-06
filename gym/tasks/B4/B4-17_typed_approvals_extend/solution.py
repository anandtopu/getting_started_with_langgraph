"""Extend typed approvals: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"decision": "approve", "amount_cents": 50000}


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    effects = []

    @tool
    def propose_payment(amount_cents: int) -> str:
        """Record a synthetic proposal after approval; never contact a payment service."""
        if type(amount_cents) is not int or amount_cents < 0:
            raise ValueError("Nonnegative integer cents required")
        effects.append(amount_cents)
        return "Synthetic proposal recorded"

    model = get_chat_model(
        responses=[
            AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "propose_payment",
                        "args": {"amount_cents": case["amount_cents"]},
                        "id": "proposal-1",
                    }
                ],
            ),
            AIMessage(content="The proposal review is complete."),
        ]
    )
    agent = create_agent(
        model=model,
        tools=[propose_payment],
        checkpointer=InMemorySaver(),
        middleware=[
            HumanInTheLoopMiddleware(
                interrupt_on={"propose_payment": {"allowed_decisions": ["approve", "reject"]}},
                interrupt_mode="per_call",
            )
        ],
    )
    config = {"configurable": {"thread_id": "typed-review"}}
    paused = agent.invoke(
        {"messages": [HumanMessage(content="Review the proposed payment.")]}, config, version="v2"
    )
    pending = paused.interrupts[0]
    schema_present = bool(pending.response_schema)
    decision = {"type": case["decision"]}
    if case["decision"] == "reject":
        decision["message"] = "The proposal is not approved."
    agent.invoke(Command(resume={pending.id: decision}), config, version="v2")
    return {
        "schema_present": schema_present,
        "effects": effects,
        "interrupt_type": pending.value["type"],
    }


def run_batch(cases: list[dict]) -> list[dict]:
    """Preview independent claims in order; one rejected input must not lose its siblings.

    This sequential interface favors isolation over throughput. It is not a shared
    checkpoint thread or a promise of transaction atomicity.
    """
    from copy import deepcopy

    from common.pretty import safe_value

    results = []
    for case in cases:
        try:
            results.append({"value": safe_value(run(deepcopy(case)))})
        except Exception as error:
            results.append({"error": type(error).__name__})
    return results


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
