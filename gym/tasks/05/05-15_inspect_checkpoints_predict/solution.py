"""Predict inspect checkpoints across the declared cases. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"amount_cents": 100000, "corrected_amount": 200000, "durability": "sync"}


class State(TypedDict):
    amount_cents: int
    route: str


def normalize(state: State) -> dict:
    return {"amount_cents": int(state["amount_cents"])}


def decide(state: State) -> dict:
    return {"route": "fast_track" if state["amount_cents"] <= 100000 else "standard"}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("normalize", normalize)
    graph.add_node("decide", decide)
    graph.add_edge(START, "normalize")
    graph.add_edge("normalize", "decide")
    graph.add_edge("decide", END)
    return graph.compile(checkpointer=InMemorySaver())


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    graph = build_graph()
    config = {"configurable": {"thread_id": "audit-claim"}}
    original = graph.invoke(
        {"amount_cents": case["amount_cents"]}, config, version="v2", durability=case["durability"]
    ).value
    history = list(graph.get_state_history(config))
    corrected = graph.update_state(
        config, {"amount_cents": case["corrected_amount"]}, as_node="normalize"
    )
    snapshot = graph.get_state(corrected)
    result = graph.invoke(None, corrected, version="v2").value
    return {
        "original": original["route"],
        "corrected": result["route"],
        "pending_after_edit": list(snapshot.next),
        "parent_exists": snapshot.parent_config is not None,
        "saved_steps": sorted(item.metadata["step"] for item in history),
    }


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"amount_cents": 100000, "corrected_amount": 200000, "durability": "sync"},
        {"amount_cents": 200000, "corrected_amount": 50000, "durability": "sync"},
        {"amount_cents": 100000, "corrected_amount": 200000, "durability": "async"},
        {"amount_cents": 100000, "corrected_amount": 200000, "durability": "exit"},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
