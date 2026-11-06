"""Diagnose replay and fork from execution evidence. Run this file with Python. No live model or network."""

from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from common.pretty import print_state

DEFAULT_CASE = {"amount_cents": 100000, "corrected_amount": 600000}


class State(TypedDict):
    amount_cents: int
    route: str
    approved: bool


def read_evidence(state: State) -> dict:
    return {"amount_cents": state["amount_cents"]}


def decide(state: State) -> dict:
    return {"route": "fast_track" if state["amount_cents"] <= 100000 else "specialist"}


def review(state: State) -> dict:
    return {"approved": interrupt({"route": state["route"]}) is True}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("read_evidence", read_evidence)
    graph.add_node("decide", decide)
    graph.add_node("review", review)
    graph.add_edge(START, "read_evidence")
    graph.add_edge("read_evidence", "decide")
    graph.add_edge("decide", "review")
    graph.add_edge("review", END)
    return graph.compile(checkpointer=InMemorySaver())


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    graph = build_graph()
    config = {"configurable": {"thread_id": "disputed-claim"}}
    graph.invoke({"amount_cents": case["amount_cents"]}, config, version="v2")
    original = graph.invoke(Command(resume=True), config, version="v2").value
    original_config = graph.get_state(config).config
    history = list(graph.get_state_history(config))
    historical = next(snapshot for snapshot in history if snapshot.next == ("decide",))
    replay = graph.invoke(None, historical.config, version="v2")
    fork_config = graph.update_state(
        historical.config, {"amount_cents": case["corrected_amount"]}, as_node="read_evidence"
    )
    fork_snapshot = graph.get_state(fork_config)
    fork = graph.invoke(None, historical.config, version="v2")
    return {
        "original_route": original["route"],
        "fork_route": fork.value["route"],
        "replay_prompts": len(replay.interrupts),
        "fork_prompts": len(fork.interrupts),
        "original_unchanged": graph.get_state(original_config).values == original,
        "fork_parent_is_historical": fork_snapshot.parent_config["configurable"]["checkpoint_id"]
        == historical.config["configurable"]["checkpoint_id"],
    }


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"amount_cents": 100000, "corrected_amount": 600000},
        {"amount_cents": 200000, "corrected_amount": 50000},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Replay the new fork configuration, not its uncorrected parent.",
    }


if __name__ == "__main__":
    main()
