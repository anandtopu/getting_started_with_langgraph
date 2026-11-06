"""Claims Copilot v10: Keep injected claim text from authorizing payouts or crossing customer boundaries. No live model or external effects."""

from common.pretty import print_state


def run() -> dict:
    from common.app_demo import run_demo

    return {"approved": run_demo(approve=True), "rejected": run_demo(approve=False)}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
