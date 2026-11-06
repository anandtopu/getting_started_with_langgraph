"""Claims Copilot v01: Accumulate validation findings without losing earlier evidence. No live model or external effects."""

from common.copilot import v01 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    result = copilot.run({**load_submission(1), "description": "", "loss_date": None})
    return {"missing": result["missing"], "findings": result["findings"], "audit": result["audit"]}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
