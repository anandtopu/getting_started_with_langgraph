"""Extend supervisor tools: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {
    "question": "Review policy and fraud evidence.",
    "private_note": "Synthetic phone: 555-0100",
}


def build_graph(seen: list[dict]):
    def specialist(role: str, evidence: str) -> str:
        seen.append({"role": role, "input": evidence})
        agent = create_agent(
            model=get_chat_model(
                responses=[AIMessage(content=role + ": evidence requires review")]
            ),
            tools=[],
            system_prompt="Use only the supplied synthetic evidence.",
        )
        return (
            agent.invoke({"messages": [HumanMessage(content=evidence)]}, version="v2")
            .value["messages"][-1]
            .content
        )

    @tool
    def policy_expert() -> str:
        """Ask the policy expert about the scoped synthetic deductible."""
        return specialist("policy", "Deductible: 100000 cents")

    @tool
    def fraud_analyst() -> str:
        """Ask the fraud analyst to inspect only document-evidence availability."""
        return specialist("fraud", "Contractor estimate is missing")

    model = get_chat_model(
        responses=[
            AIMessage(
                content="",
                tool_calls=[
                    {"name": "policy_expert", "args": {}, "id": "policy-1"},
                    {"name": "fraud_analyst", "args": {}, "id": "fraud-1"},
                ],
            ),
            AIMessage(content="Request the missing estimate before final policy review."),
        ]
    )
    return create_agent(model=model, tools=[policy_expert, fraud_analyst])


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    seen = []
    # Private notes are intentionally not forwarded to either specialist.
    result = (
        build_graph(seen)
        .invoke({"messages": [HumanMessage(content=case["question"])]}, version="v2")
        .value
    )
    return {
        "specialists": sorted(seen, key=lambda item: (item["role"], item["input"])),
        "tool_names": sorted(
            message.name for message in result["messages"] if message.type == "tool"
        ),
        "reports": sorted(
            message.content for message in result["messages"] if message.type == "tool"
        ),
        "final": result["messages"][-1].content,
        "private_note_leaked": any(case["private_note"] in item["input"] for item in seen),
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
