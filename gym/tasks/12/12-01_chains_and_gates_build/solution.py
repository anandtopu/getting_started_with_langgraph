"""Build chains and gates: Reject contradictory extracted facts before drafting.. Run this file with Python. No live model or network."""

import json
from typing import Literal, TypedDict

from langchain_core.messages import AIMessage
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, Field, StrictInt

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"category": "policy", "policy_deductible": 100000, "extracted_deductible": 100000}


class Classification(BaseModel):
    category: Literal["policy", "documents"]
    deductible_cents: StrictInt = Field(ge=0)


class Letter(BaseModel):
    text: str = Field(min_length=1)
    deductible_cents: StrictInt = Field(ge=0)


class State(TypedDict):
    category: str
    extracted_deductible: int
    draft: dict
    accepted: bool


def build_graph(case: dict | None = None):
    case = DEFAULT_CASE if case is None else case
    classifier = get_chat_model(
        responses=[
            AIMessage(
                content=json.dumps(
                    {"category": case["category"], "deductible_cents": case["extracted_deductible"]}
                )
            )
        ]
    ).with_structured_output(Classification)
    drafter = get_chat_model(
        responses=[
            AIMessage(
                content=json.dumps(
                    {
                        "text": "Thank you for the synthetic claim. We will review your evidence.",
                        "deductible_cents": case["policy_deductible"],
                    }
                )
            )
        ]
    ).with_structured_output(Letter)

    def classify(state: State) -> dict:
        facts = classifier.invoke("Classify this claim question and extract its deductible.")
        return {"category": facts.category, "extracted_deductible": facts.deductible_cents}

    def draft(state: State) -> dict:
        return {
            "draft": drafter.invoke(
                "Draft a factual letter about " + state["category"]
            ).model_dump()
        }

    def gate(state: State) -> dict:
        return {"accepted": state["extracted_deductible"] == case["policy_deductible"]}

    def next_step(state: State) -> str:
        return "draft" if state["accepted"] else END

    graph = StateGraph(State)
    graph.add_node("classify", classify)
    graph.add_node("draft", draft)
    graph.add_node("gate", gate)
    graph.add_edge(START, "classify")
    graph.add_edge("classify", "gate")
    graph.add_conditional_edges("gate", next_step, {"draft": "draft", END: END})
    graph.add_edge("draft", END)
    return graph.compile()


def run(case: dict | None = None) -> dict:
    return build_graph(case).invoke({}, version="v2").value


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
