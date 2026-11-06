"""Build worker reliability: Use the same business effect identity after worker replacement.. Run this file with Python. No live model or network."""

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
                "first-payment:" + case["claim_id"], {"amount_cents": case["amount_cents"]}
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


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    return asyncio.run(arun(dict(DEFAULT_CASE if case is None else case)))


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
