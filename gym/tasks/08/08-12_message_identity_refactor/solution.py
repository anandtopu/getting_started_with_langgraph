"""Refactor message identity: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

from langchain_core.messages import AIMessage, HumanMessage, RemoveMessage, ToolMessage
from langgraph.graph import END, START, MessagesState, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"text": "Corrected: pipe burst", "remove_customer": True}


def build_graph(case: dict | None = None):
    case = DEFAULT_CASE if case is None else case

    def correct(state: MessagesState) -> dict:
        return {"messages": [HumanMessage(content=case["text"], id="customer-1")]}

    def minimize(state: MessagesState) -> dict:
        return {"messages": [RemoveMessage(id="customer-1")]} if case["remove_customer"] else {}

    graph = StateGraph(MessagesState)
    graph.add_node("correct", correct)
    graph.add_node("minimize", minimize)
    graph.add_edge(START, "correct")
    graph.add_edge("correct", "minimize")
    graph.add_edge("minimize", END)
    return graph.compile()


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
    messages = [
        HumanMessage(content="Original claim", id="customer-1"),
        AIMessage(
            content="",
            id="agent-1",
            tool_calls=[{"name": "lookup_policy", "args": {}, "id": "call-1"}],
        ),
        ToolMessage(content="Synthetic policy found", tool_call_id="call-1", id="tool-1"),
    ]
    output = build_graph(case).invoke({"messages": messages}, version="v2").value
    return {
        "messages": [
            {"role": item.type, "id": item.id, "text": item.content} for item in output["messages"]
        ],
        "paired": output["messages"][-1].tool_call_id == "call-1",
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
