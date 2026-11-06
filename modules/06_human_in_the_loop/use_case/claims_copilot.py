"""Claims Copilot v03: Require adjuster approval for payouts above $5,000. No live model or external effects."""

from common.copilot import v03 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    claim = {**load_submission(1), "amount_cents": 600000}
    return {
        "approved": copilot.run(claim, approved=True)["approval_reason"],
        "rejected": copilot.run(claim, approved=False)["approval_reason"],
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
