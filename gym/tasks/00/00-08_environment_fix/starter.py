"""Fix environment: A missing provider is a problem only when live mode was requested.. Run this file with Python. No live model or network."""

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


# YOUR CODE HERE: repair the contract described in task.md.
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
    if not case["provider_ready"]:
        errors.append("Optional live provider is not configured")
    return {"ready": not errors, "errors": errors, "mode": "live" if case["live"] else "offline"}


def main() -> None:
    try:
        print_state(run(inspect_environment()))
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
