"""Extend recovery policies: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

import asyncio
from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.errors import GraphDrained, NodeError
from langgraph.graph import END, START, StateGraph
from langgraph.runtime import RunControl
from langgraph.types import Command, RetryPolicy, TimeoutPolicy

from common.pretty import print_state

DEFAULT_CASE = {"failures": 1, "timeout": False, "drain": True}


class State(TypedDict):
    status: str
    error_type: str
    finished: bool


def build_graph(case: dict, attempts: list, control: RunControl):
    async def fetch_estimate(state: State) -> dict:
        attempts.append("attempt")
        if case["timeout"]:
            await asyncio.Event().wait()
        if len(attempts) <= case["failures"]:
            raise ConnectionError("Synthetic contractor service unavailable")
        if case["drain"]:
            control.request_drain("maintenance")
        return {"status": "estimate_received"}

    def recover(state: State, error: NodeError) -> Command:
        return Command(
            update={"status": "manual_review", "error_type": type(error.error).__name__},
            goto="finalize",
        )

    graph = StateGraph(State)
    graph.add_node(
        "fetch_estimate",
        fetch_estimate,
        retry_policy=RetryPolicy(
            max_attempts=2, initial_interval=0, jitter=False, retry_on=ConnectionError
        ),
        timeout=TimeoutPolicy(run_timeout=0.1),
        error_handler=recover,
    )
    graph.add_node("finalize", lambda state: {"finished": True})
    graph.add_edge(START, "fetch_estimate")
    graph.add_edge("fetch_estimate", "finalize")
    graph.add_edge("finalize", END)
    return graph.compile(checkpointer=InMemorySaver())


async def arun(case: dict) -> dict:
    attempts, control = [], RunControl()
    graph = build_graph(case, attempts, control)
    config = {"configurable": {"thread_id": "contractor-recovery"}}
    drained = False
    try:
        result = await graph.ainvoke({"finished": False}, config, control=control, version="v2")
    except GraphDrained:
        drained = True
        result = await graph.ainvoke(None, config, version="v2")
    return {**result.value, "attempts": len(attempts), "drained": drained}


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    return asyncio.run(arun(dict(DEFAULT_CASE if case is None else case)))


def run_batch(cases: list[dict]) -> list[dict]:
    return []


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
