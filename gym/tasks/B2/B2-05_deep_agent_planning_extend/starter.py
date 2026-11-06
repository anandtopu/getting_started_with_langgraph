"""Extend deep agent planning: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from langchain_core.messages import AIMessage, HumanMessage

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"first_status": "in_progress", "include_planning": True}


# YOUR CODE HERE: repair the contract described in task.md.
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


def run_batch(cases: list[dict]) -> list[dict]:
    return []


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
