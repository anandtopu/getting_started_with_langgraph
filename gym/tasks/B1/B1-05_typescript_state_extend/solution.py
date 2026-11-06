"""Extend typescript state: Handle an empty normalized description as missing information.. Run this file with Python. No live model or network."""

from pathlib import Path

from common.pretty import print_state
from common.typescript import run_typescript

DEFAULT_CASE = {"claim_id": "CLM-0001", "description": "  Pipe burst  ", "amount_cents": 125000}


def run(case: dict | None = None) -> dict:
    return run_typescript(
        Path(__file__).with_suffix(".ts"), dict(DEFAULT_CASE if case is None else case)
    )


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
