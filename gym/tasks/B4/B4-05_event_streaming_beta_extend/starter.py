"""Extend event streaming beta: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

import json

from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import END, START, MessagesState, StateGraph

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"text": "Synthetic claim review is complete."}


def build_graph(text="Synthetic claim review is complete."):
    model = get_chat_model(responses=[AIMessage(content=text, id="notice")])
    child = (
        StateGraph(MessagesState)
        .add_node("notify", lambda state: {"messages": [model.invoke(state["messages"])]})
        .add_edge(START, "notify")
        .add_edge("notify", END)
        .compile(name="claim_notice")
    )
    graph = (
        StateGraph(MessagesState)
        .add_node("notice", child)
        .add_edge(START, "notice")
        .add_edge("notice", END)
    )
    return graph.compile(name="claim_parent")


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    stream = build_graph(case["text"]).stream_events(
        {"messages": [HumanMessage(content="Update this claim.")]}, version="v3"
    )
    texts = [str(message.text) for child in stream.subgraphs for message in child.messages]
    output = stream.output
    raw = build_graph(case["text"]).stream_events(
        {"messages": [HumanMessage(content="Update this claim.")]}, version="v3"
    )
    events = list(raw)
    tool_model = get_chat_model(
        responses=[
            AIMessage(
                content="",
                tool_calls=[
                    {"name": "lookup_policy", "args": {"policy_id": "POL-0001"}, "id": "policy-1"}
                ],
            )
        ]
    )
    tool_graph = (
        StateGraph(MessagesState)
        .add_node(
            "propose_lookup", lambda state: {"messages": [tool_model.invoke(state["messages"])]}
        )
        .add_edge(START, "propose_lookup")
        .add_edge("propose_lookup", END)
        .compile()
    )
    tool_stream = tool_graph.stream_events(
        {"messages": [HumanMessage(content="Propose a policy lookup.")]}, version="v3"
    )
    deltas = [chunk for message in tool_stream.messages for chunk in message.tool_calls]
    # KEY IDEA: arguments are deltas, not complete JSON until the call is finished.
    arguments = "".join(chunk["args"] for chunk in deltas)
    return {
        "texts": texts,
        "final": output["messages"][-1].text,
        "tool_arguments": json.loads(arguments),
        "tool_delta_count": len(deltas),
        "channels": sorted({event["method"] for event in events}),
        "nested": any(event["params"]["namespace"] for event in events),
        "beta": True,
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
