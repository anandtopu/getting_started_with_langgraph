"""Refactor compose stack: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

import yaml

from common.config import ROOT
from common.pretty import print_state

DEFAULT_CASE = {"public_bind": False, "remove_healthcheck": False}


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
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


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
