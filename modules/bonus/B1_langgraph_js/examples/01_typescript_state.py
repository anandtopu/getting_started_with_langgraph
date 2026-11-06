"""Python gym bridge to the adjacent real TypeScript implementation. No live model.

Run: uv run --no-sync python modules/bonus/B1_langgraph_js/examples/01_typescript_state.py
Install Node dependencies with npm ci first. The adjacent .ts file is the learner implementation.
"""

from pathlib import Path

from common.pretty import print_state
from common.typescript import run_typescript

DEFAULT_CASE = {"claim_id": "CLM-0001", "description": "  Pipe burst  ", "amount_cents": 125000}


def run(case: dict | None = None) -> dict:
    return run_typescript(
        Path(__file__).with_suffix(".ts"), dict(DEFAULT_CASE if case is None else case)
    )


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
