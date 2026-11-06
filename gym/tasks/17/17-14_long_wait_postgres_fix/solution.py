"""Fix long wait postgres: Compute elapsed business time from explicit dates.. Run this file with Python. No live model or network."""

from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "received_on": "2026-01-04", "document_id": "DOC-001"}


class State(TypedDict):
    claim_id: str
    requested_on: str
    received_on: str
    document_id: str
    waited_days: int


def build_graph(checkpointer):
    def wait_for_document(state: State) -> dict:
        response = interrupt({"claim_id": state["claim_id"], "need": "contractor_estimate"})
        if not isinstance(response, dict) or not response.get("document_id"):
            raise ValueError("An estimate document ID is required")
        elapsed = (
            date.fromisoformat(response["received_on"]) - date.fromisoformat(state["requested_on"])
        ).days
        if elapsed < 0:
            raise ValueError("Receipt cannot precede the request")
        return {
            "document_id": response["document_id"],
            "received_on": response["received_on"],
            "waited_days": elapsed,
        }

    graph = StateGraph(State)
    graph.add_node("wait_for_document", wait_for_document)
    graph.add_edge(START, "wait_for_document")
    graph.add_edge("wait_for_document", END)
    return graph.compile(checkpointer=checkpointer)


def postgres_roundtrip(connection_string: str, case: dict) -> dict:
    from langgraph.checkpoint.postgres import PostgresSaver

    config = {"configurable": {"thread_id": case["claim_id"]}}
    # setup belongs in migrations/startup, never on every production request.
    with PostgresSaver.from_conn_string(connection_string) as saver:
        saver.setup()
        build_graph(saver).invoke(
            {"claim_id": case["claim_id"], "requested_on": "2026-01-01"}, config, version="v2"
        )
    with PostgresSaver.from_conn_string(connection_string) as saver:
        return build_graph(saver).invoke(Command(resume=case), config, version="v2").value


async def async_postgres_roundtrip(connection_string: str, case: dict) -> dict:
    from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

    config = {"configurable": {"thread_id": "async-" + case["claim_id"]}}
    async with AsyncPostgresSaver.from_conn_string(connection_string) as saver:
        await saver.setup()
        graph = build_graph(saver)
        await graph.ainvoke(
            {"claim_id": case["claim_id"], "requested_on": "2026-01-01"}, config, version="v2"
        )
        return (await graph.ainvoke(Command(resume=case), config, version="v2")).value


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    config = {"configurable": {"thread_id": case["claim_id"]}}
    with TemporaryDirectory(prefix="larkspur-wait-") as directory:
        path = str(Path(directory) / "wait.db")
        with SqliteSaver.from_conn_string(path) as saver:
            paused = build_graph(saver).invoke(
                {"claim_id": case["claim_id"], "requested_on": "2026-01-01"}, config, version="v2"
            )
        with SqliteSaver.from_conn_string(path) as saver:
            result = build_graph(saver).invoke(Command(resume=case), config, version="v2")
        return {"interrupts": len(paused.interrupts), **result.value}


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
