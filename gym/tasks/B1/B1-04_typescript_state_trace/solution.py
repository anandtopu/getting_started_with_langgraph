"""Trace typescript state: Preserve Python's inclusive fast-track boundary.. Run this file with Python. No live model or network."""

from pathlib import Path

from common.pretty import print_state
from common.typescript import run_typescript

DEFAULT_CASE = {"claim_id": "CLM-0001", "description": "  Pipe burst  ", "amount_cents": 125000}


def scenario(case: dict | None = None) -> dict:
    return run_typescript(
        Path(__file__).with_suffix(".ts"), dict(DEFAULT_CASE if case is None else case)
    )


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"amount_cents": 125000, "claim_id": "CLM-0001", "description": "  Pipe burst  "},
        {"amount_cents": 100000, "claim_id": "CLM-0001", "description": "  Pipe burst  "},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Preserve Python's inclusive fast-track boundary.",
    }


if __name__ == "__main__":
    main()
