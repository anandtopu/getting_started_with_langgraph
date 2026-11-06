"""Claims Copilot v01: Route claims to fast-track, standard, or specialist handling. No live model or external effects."""

from common.copilot import v01 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    return {
        str(amount): copilot.run({**load_submission(1), "amount_cents": amount})["route"]
        for amount in (100000, 100001, 500001)
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
