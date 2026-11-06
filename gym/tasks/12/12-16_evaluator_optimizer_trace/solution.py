"""Trace evaluator optimizer: Require the authoritative deductible fact.. Run this file with Python. No live model or network."""

import operator
from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage
from langgraph.graph import END, START, StateGraph

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {
    "drafts": ["Your deductible is 90000 cents.", "Thank you. Your deductible is 100000 cents."],
    "budget": 3,
}


class State(TypedDict):
    draft: str
    attempts: int
    budget: int
    accepted: bool
    feedback: list[str]
    history: Annotated[list[dict], operator.add]


def build_graph(drafts: list[str], budget: int):
    if not drafts or type(budget) is not int or not 1 <= budget <= 10:
        raise ValueError("Provide drafts and a budget from one to ten")
    responses = [AIMessage(content=drafts[min(index, len(drafts) - 1)]) for index in range(budget)]
    model = get_chat_model(responses=responses)

    def write_letter(state: State) -> dict:
        response = model.invoke(
            "Revise the letter using this feedback: " + ", ".join(state["feedback"])
        )
        return {"draft": response.content, "attempts": state["attempts"] + 1}

    def evaluate(state: State) -> dict:
        feedback = []
        if False:
            feedback.append("deductible_fact")
        if "thank" not in state["draft"].lower():
            feedback.append("respectful_tone")
        return {
            "feedback": feedback,
            "accepted": not feedback,
            "history": [{"attempt": state["attempts"], "feedback": feedback}],
        }

    def continue_or_stop(state: State) -> str:
        return END if state["accepted"] or state["attempts"] >= state["budget"] else "write_letter"

    graph = StateGraph(State)
    graph.add_node("write_letter", write_letter)
    graph.add_node("evaluate", evaluate)
    graph.add_edge(START, "write_letter")
    graph.add_edge("write_letter", "evaluate")
    graph.add_conditional_edges(
        "evaluate", continue_or_stop, {"write_letter": "write_letter", END: END}
    )
    return graph.compile()


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    result = (
        build_graph(case["drafts"], case["budget"])
        .invoke(
            {"attempts": 0, "budget": case["budget"], "feedback": [], "history": []},
            {"recursion_limit": 30},
            version="v2",
        )
        .value
    )
    return {
        "accepted": result["accepted"],
        "attempts": result["attempts"],
        "history": result["history"],
        "stop_reason": "accepted" if result["accepted"] else "budget_exhausted",
    }


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {
            "budget": 3,
            "drafts": [
                "Your deductible is 90000 cents.",
                "Thank you. Your deductible is 100000 cents.",
            ],
        },
        {
            "budget": 1,
            "drafts": [
                "Your deductible is 90000 cents.",
                "Thank you. Your deductible is 100000 cents.",
            ],
        },
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": "Require the authoritative deductible fact."}


if __name__ == "__main__":
    main()
