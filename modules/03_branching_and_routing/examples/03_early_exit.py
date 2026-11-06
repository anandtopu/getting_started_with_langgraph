"""END is a valid routing destination. No LLM or external effects.

Run: uv run python modules/03_branching_and_routing/examples/03_early_exit.py
Expected: duplicates and invalid amounts stop before assignment.
"""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "amount_cents": 0, "duplicate_of": None}


class State(TypedDict):
    claim_id: str
    amount_cents: int
    duplicate_of: str | None
    reason: str
    assigned: bool


def screen(state: State) -> dict:
    amount = state["amount_cents"]
    reason = (
        "duplicate"
        if state["duplicate_of"]
        else "invalid"
        if type(amount) is not int or amount < 0
        else "eligible"
    )
    return {"reason": reason, "assigned": False}


def next_step(state: State) -> str:
    return "assign" if state["reason"] == "eligible" else END


def assign(state: State) -> dict:
    return {"assigned": True}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("screen", screen)
    graph.add_node("assign", assign)
    graph.add_edge(START, "screen")
    graph.add_conditional_edges("screen", next_step, {"assign": "assign", END: END})
    graph.add_edge("assign", END)
    return graph.compile()


def run(case: dict | None = None) -> dict:
    return build_graph().invoke(dict(DEFAULT_CASE if case is None else case), version="v2").value


def main() -> None:
    print_state(run())
    print_state(run({**DEFAULT_CASE, "duplicate_of": "CLM-0099"}))


if __name__ == "__main__":
    main()
