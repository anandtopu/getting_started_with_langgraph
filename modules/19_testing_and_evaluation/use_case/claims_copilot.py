"""Claims Copilot v09: Prevent regressions in claims decisions and tool behavior. No live model or external effects."""

from common.pretty import print_state


def run() -> dict:
    from common.evaluation import evaluate_file

    return evaluate_file("eval/routing.jsonl")


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
