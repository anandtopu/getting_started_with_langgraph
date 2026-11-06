"""Claims Copilot v11: Implement a small superstep runner to understand the real runtime. No live model or external effects."""

from common.pretty import print_state


def run() -> dict:
    from common.config import ROOT
    from common.loading import load_module

    return load_module(ROOT / "modules/bonus/B3_mini_langgraph/examples/02_mini_reducers.py").run()


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
