"""Compare a plain checklist with a graph. No LLM, keys, or charges.

Run: uv run python modules/00_setup/examples/01_plain_checklist.py
Expected: both implementations agree on ready, needs_information, and duplicate.
"""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common.claims import checklist
from common.gym_fixtures import checklist_cases
from common.pretty import print_state


class State(TypedDict):
    claim: dict
    decision: dict


def decide(state: State) -> dict:
    return {"decision": checklist(state["claim"])}


def build_graph():
    builder = StateGraph(State)
    builder.add_node("check_claim", decide)
    builder.add_edge(START, "check_claim")
    builder.add_edge("check_claim", END)
    return builder.compile()


def run() -> dict:
    graph = build_graph()
    plain = [checklist(claim) for claim in checklist_cases()]
    graphed = [
        graph.invoke({"claim": claim}, version="v2").value["decision"]
        for claim in checklist_cases()
    ]
    assert plain == graphed
    return {"equivalent": True, "statuses": [row["status"] for row in plain]}


def main() -> None:
    print_state(run())
    print(build_graph().get_graph().draw_mermaid())


if __name__ == "__main__":
    main()
