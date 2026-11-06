"""Extend compose stack: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

import yaml

from common.config import ROOT
from common.pretty import print_state

DEFAULT_CASE = {"public_bind": False, "remove_healthcheck": False}


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    stack = yaml.safe_load((ROOT / "compose.yaml").read_text("utf-8"))
    services = stack["services"]
    if case["public_bind"]:
        services["api"]["ports"] = ["8000:8000"]
    if case["remove_healthcheck"]:
        services["postgres"].pop("healthcheck")
    errors = []
    if "healthcheck" not in services["postgres"]:
        errors.append("postgres_readiness_missing")
    if any(
        not binding.startswith("127.0.0.1:")
        for name in ("api", "ui")
        for binding in services[name]["ports"]
    ):
        errors.append("unexpected_public_port")
    return {
        "services": sorted(services),
        "valid": not errors,
        "errors": errors,
        "api_waits_for_database": services["api"]["depends_on"]["postgres"]["condition"]
        == "service_healthy",
    }


def run_batch(cases: list[dict]) -> list[dict]:
    return []


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
