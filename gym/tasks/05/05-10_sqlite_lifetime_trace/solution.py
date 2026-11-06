"""Diagnose sqlite lifetime from execution evidence. Run this file with Python. No live model or network."""

import json
import operator
import sys
import tempfile
from pathlib import Path
from typing import Annotated, TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph

from common.config import ROOT
from common.pretty import print_state
from common.process import offline_environment, run_process

DEFAULT_CASE = {"claim_id": "CLM-0001"}


class State(TypedDict):
    claim_id: str
    notes: Annotated[list[str], operator.add]
    status: str


def save(state: State) -> dict:
    return {"status": "saved"}


def build_graph(saver):
    graph = StateGraph(State)
    graph.add_node("save", save)
    graph.add_edge(START, "save")
    graph.add_edge("save", END)
    return graph.compile(checkpointer=saver)


def session(database: str, phase: str, claim_id: str) -> dict:
    config = {"configurable": {"thread_id": claim_id}}
    payload = {
        "claim_id": claim_id,
        "notes": ["received" if phase == "start" else "estimate attached"],
    }
    with SqliteSaver.from_conn_string(database) as saver:
        graph = build_graph(saver)
    result = graph.invoke(payload, config, version="v2").value
    return result


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    with tempfile.TemporaryDirectory(prefix="larkspur-session-") as temporary:
        database = Path(temporary) / "checkpoints.sqlite"
        outputs = []
        for phase in ("start", "continue"):
            result = run_process(
                [
                    sys.executable,
                    "-m",
                    "common.offline",
                    str(Path(__file__).resolve()),
                    "--worker",
                    str(database),
                    phase,
                    case["claim_id"],
                ],
                cwd=ROOT,
                timeout=20,
                env=offline_environment(),
            )
            if result.returncode:
                raise RuntimeError(result.stdout)
            outputs.append(json.loads(result.stdout))
        database.rename(database.with_suffix(".closed"))
        return {
            "first_notes": outputs[0]["notes"],
            "second_notes": outputs[1]["notes"],
            "closed": True,
        }


def main() -> None:
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "--worker":
            print(json.dumps(session(*sys.argv[2:])))
        else:
            print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


def run() -> dict:
    observations = []
    for case in [{"claim_id": "CLM-0001"}, {"claim_id": "CLM-0199"}]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "A compiled graph cannot use a saver whose connection has closed.",
    }


if __name__ == "__main__":
    main()
