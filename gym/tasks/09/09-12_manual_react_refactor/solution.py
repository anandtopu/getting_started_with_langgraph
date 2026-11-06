"""Refactor manual react: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"policy_id": "POL-0001", "recursion_limit": 12}


@tool
def policy_deductible(policy_id: str) -> str:
    """Return the deductible from the small synthetic policy fixture."""
    if policy_id != "POL-0001":
        raise ValueError("Unknown policy")
    return "100000 cents"


def build_graph(policy_id: str = "POL-0001"):
    model = get_chat_model(
        responses=[
            AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "policy_deductible",
                        "args": {"policy_id": policy_id},
                        "id": "policy-1",
                    }
                ],
            ),
            AIMessage(content="Use the tool result as evidence; this is not payment approval."),
        ]
    ).bind_tools([policy_deductible])

    def call_model(state: MessagesState) -> dict:
        return {"messages": [model.invoke(state["messages"])]}

    graph = StateGraph(MessagesState)
    graph.add_node("call_model", call_model)
    graph.add_node("tools", ToolNode([policy_deductible], handle_tool_errors=True))
    graph.add_edge(START, "call_model")
    graph.add_conditional_edges("call_model", tools_condition, {"tools": "tools", END: END})
    graph.add_edge("tools", "call_model")
    return graph.compile()


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
    result = (
        build_graph(case["policy_id"])
        .invoke(
            {"messages": [HumanMessage(content="Check the policy deductible.")]},
            {"recursion_limit": case["recursion_limit"]},
            version="v2",
        )
        .value
    )
    return {
        "roles": [message.type for message in result["messages"]],
        "tool_results": [
            message.content for message in result["messages"] if message.type == "tool"
        ],
        "final": result["messages"][-1].content,
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
