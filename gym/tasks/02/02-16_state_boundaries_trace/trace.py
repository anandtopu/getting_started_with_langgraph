"""Diagnose state boundaries from execution evidence. Run this file with Python. No live model or network."""

from typing import Annotated, TypedDict

from langchain_core.messages import AnyMessage, HumanMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "text": "  Pipe burst  "}


class Input(TypedDict):
    claim_id: str
    text: str


class Output(TypedDict):
    claim_id: str
    messages: Annotated[list[AnyMessage], add_messages]


class Internal(Input, Output):
    private_notes: str


def receive(state: Internal) -> dict:
    return {
        "messages": [HumanMessage(content=state["text"], id="customer-1")],
        "private_notes": "Internal review cue",
    }


def correct_message(state: Internal) -> dict:
    return {"messages": [HumanMessage(content=state["text"].strip(), id="customer-2")]}


def build_graph():
    builder = StateGraph(Internal, input_schema=Input, output_schema=Output)
    builder.add_node("receive", receive)
    builder.add_node("correct_message", correct_message)
    builder.add_edge(START, "receive")
    builder.add_edge("receive", "correct_message")
    builder.add_edge("correct_message", END)
    return builder.compile()


def run(case: dict | None = None) -> dict:
    result = build_graph().invoke(dict(DEFAULT_CASE if case is None else case), version="v2").value
    return {
        "fields": sorted(result),
        "claim_id": result["claim_id"],
        "messages": [
            {"id": message.id, "content": message.content} for message in result["messages"]
        ],
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
