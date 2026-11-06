"""Predict typescript durable across the declared cases. Run this file with Python. No live model or network."""

from pathlib import Path

from common.pretty import print_state
from common.typescript import run_typescript

DEFAULT_CASE = {"documents": ["estimate", "receipt"], "approved": False}


def scenario(case: dict | None = None) -> dict:
    return run_typescript(
        Path(__file__).with_suffix(".ts"), dict(DEFAULT_CASE if case is None else case)
    )


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"approved": False, "documents": ["estimate", "receipt"]},
        {"approved": True, "documents": []},
        {"approved": False, "documents": ["police_report"]},
        {"approved": "yes", "documents": ["estimate", "receipt"]},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
