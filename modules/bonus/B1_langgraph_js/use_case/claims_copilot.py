"""Claims Copilot v11: Port core claim workflows and the tool loop to TypeScript. No live model or external effects."""

from common.pretty import print_state


def run() -> dict:
    from common.config import ROOT
    from common.loading import load_module

    return load_module(
        ROOT / "modules/bonus/B1_langgraph_js/examples/03_typescript_agents.py"
    ).run()


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
