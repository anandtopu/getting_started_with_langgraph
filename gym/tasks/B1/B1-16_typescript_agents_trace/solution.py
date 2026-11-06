"""Trace typescript agents: Respect the configured loop budget in both JavaScript agents.. Run this file with Python. No live model or network."""

from pathlib import Path

from common.pretty import print_state
from common.typescript import run_typescript

DEFAULT_CASE = {"policy_id": "POL-0001", "recursion_limit": 12}


def scenario(case: dict | None = None) -> dict:
    return run_typescript(
        Path(__file__).with_suffix(".ts"), dict(DEFAULT_CASE if case is None else case)
    )


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"policy_id": "POL-0001", "recursion_limit": 12},
        {"policy_id": "POL-0001", "recursion_limit": 1},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Respect the configured loop budget in both JavaScript agents.",
    }


if __name__ == "__main__":
    main()
