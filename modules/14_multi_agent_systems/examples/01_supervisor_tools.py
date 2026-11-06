"""Call narrow specialist agents as tools with private histories. Four fake calls.

Run: uv run python modules/14_multi_agent_systems/examples/01_supervisor_tools.py
Expected: the supervisor delegates policy and fraud work, then returns one conclusion.
"""

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


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
