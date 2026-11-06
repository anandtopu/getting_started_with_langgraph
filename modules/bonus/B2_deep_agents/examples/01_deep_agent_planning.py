"""Opt into TodoListMiddleware and track a real Deep Agent plan. Requires bonus extra.

Run: uv run --extra bonus python modules/bonus/B2_deep_agents/examples/01_deep_agent_planning.py
Expected: one explicit planning tool call stores two synthetic investigation tasks.
"""

from langchain_core.messages import AIMessage, HumanMessage

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"first_status": "in_progress", "include_planning": True}


def run(case: dict | None = None) -> dict:
    from deepagents import create_deep_agent
    from deepagents.backends import StateBackend
    from langchain.agents.middleware import TodoListMiddleware

    case = DEFAULT_CASE if case is None else case
    todos = [
        {"content": "Read the policy deductible", "status": case["first_status"]},
        {"content": "Review the contractor estimate", "status": "pending"},
    ]
    model = get_chat_model(
        responses=[
            AIMessage(
                content="",
                tool_calls=[{"name": "write_todos", "args": {"todos": todos}, "id": "plan-1"}],
            ),
            AIMessage(content="The policy and document investigation plan is recorded."),
        ]
    )
    agent = create_deep_agent(
        model=model,
        backend=StateBackend(),
        tools=[],
        subagents=[],
        middleware=[TodoListMiddleware()] if case["include_planning"] else [],
    )
    result = agent.invoke(
        {"messages": [HumanMessage(content="Plan a synthetic claim investigation.")]},
        {"recursion_limit": 20},
        version="v2",
    ).value
    return {
        "todos": result.get("todos", []),
        "tool_statuses": [
            message.status for message in result["messages"] if message.type == "tool"
        ],
        "final": result["messages"][-1].content,
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
