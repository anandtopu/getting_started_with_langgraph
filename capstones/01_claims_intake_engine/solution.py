"""Durable deterministic intake with parallel evidence, approval, and replay.

Run: uv run python capstones/01_claims_intake_engine/solution.py
Expected: approved true, replay_matches true, more than one checkpoint. LLM: No.
"""

from pathlib import Path
from tempfile import TemporaryDirectory

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.types import Command

from common.copilot.v03 import build_graph
from common.data import load_submission
from common.pretty import print_state


def run(case=None):
    case = {"amount_cents": 600000, "approved": True, **(case or {})}
    claim = {**load_submission(1), "amount_cents": case["amount_cents"]}
    config = {"configurable": {"thread_id": "intake-capstone"}}
    with TemporaryDirectory() as directory:
        path = str(Path(directory) / "checkpoints.db")
        with SqliteSaver.from_conn_string(path) as saver:
            graph = build_graph(saver)
            first = graph.invoke(
                {"claim": claim, "audit": [], "findings": []}, config, version="v2"
            )
            waiting = bool(first.interrupts)
        # KEY IDEA: reopen the saved thread with a new saver and graph instance.
        with SqliteSaver.from_conn_string(path) as saver:
            graph = build_graph(saver)
            if waiting:
                graph.invoke(Command(resume={"approved": case["approved"]}), config, version="v2")
            snapshot = graph.get_state(config)
            history = list(graph.get_state_history(config))
            replay = graph.invoke(None, snapshot.config, version="v2").value
            return {
                "approved": snapshot.values["approved"],
                "route": snapshot.values["route"],
                "waited": waiting,
                "checkpoints": len(history),
                "replay_matches": replay == snapshot.values,
                "findings": snapshot.values["findings"],
            }


def main():
    print_state(run())


if __name__ == "__main__":
    main()
