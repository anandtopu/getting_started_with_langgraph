"""Claims Copilot v09: Find a misrouted claim using local traces and optional Studio. No live model or external effects."""

from common.pretty import print_state


def run() -> dict:
    from common.config import ROOT
    from common.loading import load_module

    return load_module(
        ROOT / "modules/20_observability_and_debugging/examples/03_optional_tracing.py"
    ).run()


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
