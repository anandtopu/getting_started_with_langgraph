"""Claims Copilot v11: Evaluate recent changes without silently changing the core course contracts. No live model or external effects."""

from common.pretty import print_state


def run() -> dict:
    from common.config import ROOT
    from common.loading import load_module

    return load_module(ROOT / "modules/bonus/B4_whats_new/examples/03_typed_approvals.py").run()


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
