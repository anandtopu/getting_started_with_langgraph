"""Trace virtual filesystem: Deny writes outside the permitted virtual directory.. Run this file with Python. No live model or network."""

from langchain_core.messages import AIMessage, HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"path": "/claims/review.txt", "content": "Synthetic estimate requires review."}


def run(case: dict | None = None) -> dict:
    from deepagents import create_deep_agent
    from deepagents.backends import StateBackend
    from deepagents.middleware.filesystem import FilesystemPermission

    case = DEFAULT_CASE if case is None else case
    model = get_chat_model(
        responses=[
            AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "write_file",
                        "args": {"file_path": case["path"], "content": case["content"]},
                        "id": "file-1",
                    }
                ],
            ),
            AIMessage(content="The virtual write request has been processed."),
        ]
    )
    saver = InMemorySaver()
    agent = create_deep_agent(
        model=model,
        backend=StateBackend(),
        tools=[],
        subagents=[],
        checkpointer=saver,
        permissions=[
            FilesystemPermission(operations=["write"], paths=["/claims/**"], mode="allow"),
            FilesystemPermission(operations=["write"], paths=["/**"], mode="allow"),
        ],
    )
    config = {"configurable": {"thread_id": "virtual-claim"}, "recursion_limit": 20}
    result = agent.invoke(
        {"messages": [HumanMessage(content="Save this scoped investigation note.")]},
        config,
        version="v2",
    ).value
    files = agent.get_state(config).values.get("files", {})
    return {
        "paths": sorted(files),
        "contents": {path: value["content"] for path, value in files.items()},
        "tool_statuses": [
            message.status for message in result["messages"] if message.type == "tool"
        ],
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
