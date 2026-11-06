"""Claims Copilot v07: Expose the synthetic claims system through local MCP tools. No live model or external effects."""

from common.copilot import v07 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    from common.config import ROOT
    from common.loading import load_module

    mcp = load_module(ROOT / "modules/16_external_systems_and_mcp/examples/03_mcp_adapter.py").run()
    result = copilot.run(load_submission(1))
    return {"mcp_evidence": mcp["claim"], "risk_flags": result["risk_flags"]}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
