"""Evaluate setup requirements without exposing keys. No LLM or network.

Run: uv run python modules/00_setup/examples/02_environment.py
Expected: deterministic intake is ready even without a model key.
"""

import importlib.metadata
import sys
from pathlib import Path

from common.data import DATA
from common.pretty import print_state

DEFAULT_CASE = {
    "python": [3, 12],
    "packages": ["langgraph", "pytest"],
    "data_present": True,
    "live": False,
    "provider_ready": False,
}


def inspect_environment() -> dict:
    installed = []
    for package in ("langgraph", "pytest"):
        try:
            importlib.metadata.version(package)
            installed.append(package)
        except importlib.metadata.PackageNotFoundError:
            continue
    return {
        **DEFAULT_CASE,
        "python": list(sys.version_info[:2]),
        "packages": installed,
        "data_present": (DATA / "claims.db").is_file(),
        "interpreter": Path(sys.executable).name,
    }


def run(case: dict | None = None) -> dict:
    case = dict(DEFAULT_CASE if case is None else case)
    errors = []
    if not (3, 11) <= tuple(case["python"]) < (3, 15):
        errors.append("Use Python 3.11–3.14")
    for package in ("langgraph", "pytest"):
        if package not in case["packages"]:
            errors.append("Missing package: " + package)
    if not case["data_present"]:
        errors.append("Missing data/claims.db; restore the committed fixtures")
    if case["live"] and not case["provider_ready"]:
        errors.append("Optional live provider is not configured")
    return {"ready": not errors, "errors": errors, "mode": "live" if case["live"] else "offline"}


def main() -> None:
    print_state(run(inspect_environment()))


if __name__ == "__main__":
    main()
