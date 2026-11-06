"""Refactor supervisor tools: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

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


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
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


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
