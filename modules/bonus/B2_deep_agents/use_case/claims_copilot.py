"""Claims Copilot v11: Plan a larger claim investigation using explicit planning and bounded subagents. No live model or external effects."""

from common.pretty import print_state


def run() -> dict:
    from common.config import ROOT
    from common.loading import load_module

    return load_module(ROOT / "modules/bonus/B2_deep_agents/examples/03_deep_subagents.py").run()


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
