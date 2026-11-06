"""Claims Copilot v06: Draft a claim letter and improve it against known policy facts. No live model or external effects."""

from common.copilot import v06 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    result = copilot.run(load_submission(1))
    return {
        "letter": result["letter"],
        "accepted": result["letter_accepted"],
        "attempts": result["letter_attempts"],
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
