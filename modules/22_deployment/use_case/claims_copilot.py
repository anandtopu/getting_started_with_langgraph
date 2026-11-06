"""Claims Copilot v11: Run the completed Claims Copilot behind an API with durable storage and a dashboard. No live model or external effects."""

from common.pretty import print_state


def run() -> dict:
    from common.app_demo import run_demo

    return run_demo(approve=True, stale=True)


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
