"""Refactor orchestrator workers: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

import json
import operator
from typing import Annotated, Literal, TypedDict

from langchain_core.messages import AIMessage
from langgraph.graph import END, START, StateGraph
from langgraph.types import Send
from pydantic import BaseModel, Field, field_validator

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"sections": ["coverage", "deductible", "exclusions"]}
FACTS = {
    "coverage": "Water damage is a synthetic covered cause.",
    "deductible": "The synthetic deductible is 100000 cents.",
    "exclusions": "Flood needs the separate add-on.",
}


class Plan(BaseModel):
    sections: list[Literal["coverage", "deductible", "exclusions"]] = Field(max_length=3)

    @field_validator("sections")
    @classmethod
    def unique_sections(cls, value):
        if len(value) != len(set(value)):
            raise ValueError("Worker sections must be unique")
        return value


class State(TypedDict):
    sections: list[str]
    reports: Annotated[list[dict], operator.add]
    report: str


class Worker(TypedDict):
    section: str


def build_graph(sections: list[str] | None = None):
    planner = get_chat_model(
        responses=[
            AIMessage(
                content=json.dumps(
                    {"sections": DEFAULT_CASE["sections"] if sections is None else sections}
                )
            )
        ]
    ).with_structured_output(Plan)

    def plan(state: State) -> dict:
        return {
            "sections": planner.invoke("Plan the required policy explanation sections.").sections
        }

    def dispatch(state: State) -> list:
        return [Send("write_section", {"section": section}) for section in state["sections"]] or [
            "assemble"
        ]

    def write_section(state: Worker) -> dict:
        model = get_chat_model(responses=[AIMessage(content=FACTS[state["section"]])])
        text = model.invoke("Explain only the supplied synthetic policy fact.").content
        return {"reports": [{"section": state["section"], "text": text}]}

    def assemble(state: State) -> dict:
        return {
            "report": "\n".join(
                item["text"] for item in sorted(state["reports"], key=lambda item: item["section"])
            )
        }

    graph = StateGraph(State)
    graph.add_node("plan", plan)
    graph.add_node("write_section", write_section, input_schema=Worker)
    graph.add_node("assemble", assemble, defer=True)
    graph.add_edge(START, "plan")
    graph.add_conditional_edges("plan", dispatch, ["write_section", "assemble"])
    graph.add_edge("write_section", "assemble")
    graph.add_edge("assemble", END)
    return graph.compile()


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
    result = build_graph(case["sections"]).invoke({"reports": []}, version="v2").value
    return {
        "sections": sorted(item["section"] for item in result["reports"]),
        "report": result["report"],
        "model_calls": 1 + len(result["reports"]),
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
