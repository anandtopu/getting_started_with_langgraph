"""Claims Copilot v06: Remember contact preferences while keeping customer histories isolated. No live model or external effects."""

from common.copilot import v06 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    result = copilot.run(load_submission(1), preference="sms")
    return {"preference": result["preference"], "audit": result["audit"]}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
