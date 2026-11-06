"""Extend deep subagents: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from langchain_core.messages import AIMessage, HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"decision": "approve", "specialist": "policy_expert"}


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    from deepagents import create_deep_agent
    from deepagents.backends import StateBackend
    from langchain.agents.middleware import ModelCallLimitMiddleware

    case = DEFAULT_CASE if case is None else case
    specialist = get_chat_model(
        responses=[AIMessage(content="The synthetic deductible is 100000 cents.")]
    )
    supervisor = get_chat_model(
        responses=[
            AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "task",
                        "args": {
                            "description": "Explain only the synthetic deductible.",
                            "subagent_type": case["specialist"],
                        },
                        "id": "delegate-1",
                    }
                ],
            ),
            AIMessage(content="The delegation request is complete."),
        ]
    )
    agent = create_deep_agent(
        model=supervisor,
        backend=StateBackend(),
        tools=[],
        subagents=[
            {
                "name": "policy_expert",
                "description": "Explain one synthetic policy fact.",
                "system_prompt": "Read only the supplied deductible; do not authorize payment.",
                "model": specialist,
                "tools": [],
                "mode": "isolated",
            }
        ],
        middleware=[ModelCallLimitMiddleware(run_limit=3, exit_behavior="end")],
        interrupt_on={"task": {"allowed_decisions": ["approve", "reject"]}},
        checkpointer=InMemorySaver(),
    )
    config = {"configurable": {"thread_id": "deep-team"}, "recursion_limit": 30}
    paused = agent.invoke(
        {"messages": [HumanMessage(content="Ask the policy specialist.")]}, config, version="v2"
    )
    decision = {"type": case["decision"]}
    if case["decision"] == "reject":
        decision["message"] = "Do not delegate this claim."
    result = agent.invoke(Command(resume={"decisions": [decision]}), config, version="v2").value
    return {
        "paused": len(paused.interrupts),
        "tool_results": [
            message.content for message in result["messages"] if message.type == "tool"
        ],
        "final": result["messages"][-1].content,
    }


def run_batch(cases: list[dict]) -> list[dict]:
    return []


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
