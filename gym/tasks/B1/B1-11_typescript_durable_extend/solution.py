"""Extend typescript durable: Preserve a rejected approval through JavaScript resume.. Run this file with Python. No live model or network."""

from pathlib import Path

from common.pretty import print_state
from common.typescript import run_typescript

DEFAULT_CASE = {"documents": ["estimate", "receipt"], "approved": False}


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
