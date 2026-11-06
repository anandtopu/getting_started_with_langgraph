"""Refactor agent composition: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

from typing import TypedDict

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import END, START, StateGraph

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "question": "What evidence is missing?"}


class State(TypedDict):
    claim_id: str
    question: str
    explanation: str
    status: str


def build_graph():
    agent = create_agent(
        model=get_chat_model(
            responses=[AIMessage(content="Please attach a dated repair estimate.")]
        ),
        tools=[],
    )

    def explain(state: State) -> dict:
        result = agent.invoke({"messages": [HumanMessage(content=state["question"])]}, version="v2")
        return {"explanation": result.value["messages"][-1].content}

    def finalize(state: State) -> dict:
        return {"status": "awaiting_evidence"}

    graph = StateGraph(State)
    graph.add_node("explain", explain)
    graph.add_node("finalize", finalize)
    graph.add_edge(START, "explain")
    graph.add_edge("explain", "finalize")
    graph.add_edge("finalize", END)
    return graph.compile()


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
    result = build_graph().invoke(dict(case), version="v2").value
    return {"fields": sorted(result), **result}


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
