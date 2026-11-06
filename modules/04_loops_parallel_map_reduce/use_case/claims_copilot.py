"""Claims Copilot v02: Check all attached documents and combine the findings. No live model or external effects."""

from common.copilot import v02 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    claim = {**load_submission(1), "documents": ["DOC-001", "DOC-011", "DOC-021"]}
    result = copilot.run(claim)
    return {"route": result["route"], "findings": sorted(result["findings"])}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
