"""Predict worker reliability across the declared cases. Run this file with Python. No live model or network."""

import asyncio
from pathlib import Path
from tempfile import TemporaryDirectory

from common.effects import EffectLedger
from common.pretty import print_state
from common.service import BusyThread, ThreadRegistry

DEFAULT_CASE = {"claim_id": "CLM-0001", "amount_cents": 50000, "changed_payload": False}


async def arun(case):
    with TemporaryDirectory(prefix="larkspur-workers-") as directory:
        path = Path(directory) / "service.db"
        registry = ThreadRegistry(path)
        busy = False
        async with registry.guard(case["claim_id"]):
            try:
                async with registry.guard(case["claim_id"]):
                    busy = False
            except BusyThread:
                busy = True
        async with registry.guard(case["claim_id"]):
            created = registry.ledger.record(
                "payment:" + case["claim_id"], {"amount_cents": case["amount_cents"]}
            )
        restarted = EffectLedger(path)
        replayed = restarted.record(
            "payment:" + case["claim_id"],
            {"amount_cents": case["amount_cents"] + int(case["changed_payload"])},
        )
        return {
            "competing_worker_busy": busy,
            "first_created": created,
            "replay_created": replayed,
            "effects": len(restarted.rows()),
        }


def scenario(case: dict | None = None) -> dict:
    return asyncio.run(arun(dict(DEFAULT_CASE if case is None else case)))


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"amount_cents": 50000, "changed_payload": False, "claim_id": "CLM-0001"},
        {"amount_cents": 50000, "changed_payload": False, "claim_id": "CLM-0020"},
        {"amount_cents": 50000, "changed_payload": True, "claim_id": "CLM-0001"},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
