"""Python gym bridge to the adjacent real TypeScript implementation. No live model.

Run with uv run python FILE after npm ci. The .ts file is the learner implementation.
"""

from pathlib import Path

from common.pretty import print_state
from common.typescript import run_typescript

DEFAULT_CASE = {"documents": ["estimate", "receipt"], "approved": False}


def run(case: dict | None = None) -> dict:
    return run_typescript(
        Path(__file__).with_suffix(".ts"), dict(DEFAULT_CASE if case is None else case)
    )


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
