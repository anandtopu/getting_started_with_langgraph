"""Bound state-driven specialist handoffs and compare them with a single agent. Fakes only.

Run: uv run python modules/14_multi_agent_systems/examples/03_team_tradeoffs.py
Expected: a four-role team costs four fake calls; a single agent uses one.
"""

import operator
from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"budget": 4, "start_agent": "intake"}
ROLES = ["intake", "policy", "fraud", "communication"]


class State(TypedDict):
    active_agent: str
    calls: int
    budget: int
    reports: Annotated[list[str], operator.add]
    complete: bool


def build_graph():
    graph = StateGraph(State)

    def make_agent(role: str):
        def act(state: State) -> Command:
            if state["calls"] >= state["budget"]:
                return Command(goto=END, update={"complete": False})
            model = get_chat_model(responses=[AIMessage(content=role + " checked")])
            report = model.invoke("Review only your assigned claim evidence.").content
            index = ROLES.index(role)
            next_role = ROLES[index + 1] if index + 1 < len(ROLES) else END
            return Command(
                goto=next_role,
                update={
                    "active_agent": role,
                    "calls": state["calls"] + 1,
                    "reports": [report],
                    "complete": next_role == END,
                },
            )

        return act

    for role in ROLES:
        graph.add_node(role, make_agent(role), destinations=tuple(ROLES) + (END,))
    graph.add_conditional_edges(
        START, lambda state: state["active_agent"], {role: role for role in ROLES}
    )
    return graph.compile()


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    if type(case["budget"]) is not int or not 0 <= case["budget"] <= 10:
        raise ValueError("Budget must be an integer from zero to ten")
    team = (
        build_graph()
        .invoke(
            {
                "active_agent": case["start_agent"],
                "calls": 0,
                "budget": case["budget"],
                "reports": [],
                "complete": False,
            },
            {"recursion_limit": 12},
            version="v2",
        )
        .value
    )
    single = get_chat_model(
        responses=[AIMessage(content="intake, policy, fraud, communication checked")]
    ).invoke("Review all four claim concerns.")
    return {
        "team_calls": team["calls"],
        "team_complete": team["complete"],
        "reports": team["reports"],
        "single_calls": 1,
        "single_mentions_all_roles": all(role in single.content for role in ROLES),
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
