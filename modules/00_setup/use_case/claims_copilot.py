"""Claims Copilot v00: Compare a plain claim checklist with an equivalent graph. No live model or external effects."""

from common.copilot import v00 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    return {"complete": copilot.run(load_submission(1)), "missing": copilot.run(load_submission(7))}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
