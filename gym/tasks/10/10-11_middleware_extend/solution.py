"""Extend middleware: Distinguish the after hook from the before hook in lifecycle records.. Run this file with Python. No live model or network."""

from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import (
    AgentMiddleware,
    ModelCallLimitMiddleware,
    ToolCallLimitMiddleware,
)
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"model_limit": 3, "tool_limit": 1}


class AuditState(AgentState):
    observed_calls: int


class AuditMiddleware(AgentMiddleware):
    state_schema = AuditState

    def __init__(self, events: list[str]):
        self.events = events

    def before_model(self, state, runtime):
        self.events.append("before_model")
        return {"observed_calls": state.get("observed_calls", 0) + 1}

    def wrap_model_call(self, request, handler):
        self.events.append("wrap_enter")
        response = handler(request)
        self.events.append("wrap_exit")
        return response

    def after_model(self, state, runtime):
        self.events.append("after_model")


def build_graph(events: list[str], model_limit: int = 3, tool_limit: int = 1):
    @tool
    def read_policy() -> str:
        """Read one synthetic policy fact without side effects."""
        events.append("tool")
        return "Deductible: 100000 cents."

    model = get_chat_model(
        responses=[
            AIMessage(content="", tool_calls=[{"name": "read_policy", "args": {}, "id": "read-1"}]),
            AIMessage(content="Policy fact checked."),
        ]
    )
    return create_agent(
        model=model,
        tools=[read_policy],
        middleware=[
            AuditMiddleware(events),
            ModelCallLimitMiddleware(run_limit=model_limit, exit_behavior="end"),
            ToolCallLimitMiddleware(run_limit=tool_limit, exit_behavior="continue"),
        ],
    )


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    events = []
    graph = build_graph(events, case["model_limit"], case["tool_limit"])
    output = graph.invoke(
        {"messages": [HumanMessage(content="Verify the deductible.")]}, version="v2"
    ).value
    return {
        "events": events,
        "model_calls": events.count("wrap_enter"),
        "tool_calls": events.count("tool"),
        "final": output["messages"][-1].content,
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
