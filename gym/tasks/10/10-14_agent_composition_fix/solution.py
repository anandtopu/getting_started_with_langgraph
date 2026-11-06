"""Fix agent composition: Do not turn an explanation into payment approval.. Run this file with Python. No live model or network."""

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


def run(case: dict | None = None) -> dict:
    result = build_graph().invoke(dict(DEFAULT_CASE if case is None else case), version="v2").value
    return {"fields": sorted(result), **result}


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
