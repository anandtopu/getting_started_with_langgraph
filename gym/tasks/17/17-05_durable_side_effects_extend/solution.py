"""Extend durable side effects: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

import json
import os
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.func import entrypoint, task

from common.config import ROOT
from common.effects import EffectLedger
from common.pretty import print_state
from common.process import offline_environment, run_process

DEFAULT_CASE = {"claim_id": "CLM-0001", "durability": "sync"}


def worker(directory: Path, case: dict, crash: bool) -> dict:
    ledger = EffectLedger(directory / "effects.db")
    with SqliteSaver.from_conn_string(str(directory / "checkpoints.db")) as saver:

        @task
        def request_estimate(claim_id: str) -> dict:
            key = "estimate:" + claim_id
            ledger.record(key, {"claim_id": claim_id, "kind": "estimate_request"})
            if crash:
                # Simulate the hardest window: effect committed, task result not checkpointed.
                os._exit(42)
            return {"claim_id": claim_id, "request_key": key}

        @entrypoint(checkpointer=saver)
        def workflow(claim: dict) -> dict:
            return request_estimate(claim["claim_id"]).result()

        config = {"configurable": {"thread_id": case["claim_id"]}}
        saved = saver.get_tuple(config)
        # exit durability can lose all in-flight checkpoints; restart the same operation then.
        payload = None if not crash and saved is not None else case
        result = workflow.invoke(payload, config, durability=case["durability"], version="v2")
        return {"value": result.value, "effects": ledger.rows()}


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    if case["durability"] not in {"sync", "async", "exit"}:
        raise ValueError("Unknown durability mode")
    with TemporaryDirectory(prefix="larkspur-crash-") as directory:
        command = [
            sys.executable,
            "-m",
            "common.offline",
            str(Path(__file__).resolve()),
            "--worker",
            directory,
            json.dumps(case),
        ]
        crashed = run_process([*command, "crash"], cwd=ROOT, timeout=20, env=offline_environment())
        resumed = run_process([*command, "resume"], cwd=ROOT, timeout=20, env=offline_environment())
        if crashed.returncode != 42 or resumed.returncode:
            raise RuntimeError(
                "Owned crash/restart worker did not follow its contract: " + resumed.stdout[-300:]
            )
        result = json.loads(resumed.stdout.strip().splitlines()[-1])
        return {
            "crash_exit": crashed.returncode,
            "effect_count": len(result["effects"]),
            "claim_id": result["value"]["claim_id"],
            "durability": case["durability"],
        }


def run_batch(cases: list[dict]) -> list[dict]:
    """Preview independent claims in order; one rejected input must not lose its siblings.

    This sequential interface favors isolation over throughput. It is not a shared
    checkpoint thread or a promise of transaction atomicity.
    """
    from copy import deepcopy

    from common.pretty import safe_value

    results = []
    for case in cases:
        try:
            results.append({"value": safe_value(run(deepcopy(case)))})
        except Exception as error:
            results.append({"error": type(error).__name__})
    return results


def main() -> None:
    try:
        if "--worker" in sys.argv:
            index = sys.argv.index("--worker")
            print(
                json.dumps(
                    worker(
                        Path(sys.argv[index + 1]),
                        json.loads(sys.argv[index + 2]),
                        sys.argv[index + 3] == "crash",
                    )
                )
            )
        else:
            print_state(run())
    except Exception as error:
        if "--worker" in sys.argv:
            raise
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
