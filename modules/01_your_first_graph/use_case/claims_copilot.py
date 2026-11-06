"""Claims Copilot v01: Normalize a claim through a deterministic intake pipeline. No live model or external effects."""

from common.copilot import v01 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    return copilot.run({**load_submission(1), "description": "  Pipe burst  "})


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
