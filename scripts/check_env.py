"""Diagnose core setup without requiring optional services or showing secrets."""

import argparse
import importlib.metadata
import platform
import shutil
import sys

from common.config import ConfigurationError, load_settings
from common.data import DATA
from common.process import run_process


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--live", action="store_true", help="Check the chosen optional model configuration."
    )
    parser.add_argument("--docker", action="store_true", help="Check optional Docker availability.")
    arguments = parser.parse_args()
    failures = []
    print(f"Python {platform.python_version()} ({platform.system()})")
    if not (3, 11) <= sys.version_info[:2] < (3, 15):
        failures.append("Use Python 3.11–3.14; 3.12 is recommended.")
    for package in (
        "langgraph",
        "langchain-core",
        "langchain",
        "langgraph-checkpoint-sqlite",
        "pytest",
    ):
        try:
            print(f"{package}: {importlib.metadata.version(package)}")
        except importlib.metadata.PackageNotFoundError:
            failures.append(f"Missing {package}; run uv sync.")
    for path in (
        "claims.db",
        "manifest.json",
        "policies/home.md",
        "claim_submissions/claim_001.json",
    ):
        if not (DATA / path).is_file():
            failures.append(f"Missing committed synthetic fixture: data/{path}")
    if arguments.live:
        from common.models import get_chat_model

        try:
            settings = load_settings()
            print(f"Optional live provider: {settings.provider}; model: {settings.model}")
            get_chat_model(mode="live", settings=settings)
            print(
                "Provider configured. No paid generation was requested; hosted account access is not proven."
            )
        except ConfigurationError as error:
            failures.append(str(error))
    else:
        print("Ollama, provider keys, and Docker are not required for the offline course.")
    if arguments.docker:
        if not shutil.which("docker"):
            failures.append("Docker is not installed; it is optional until deployment exercises.")
        else:
            try:
                result = run_process(
                    ["docker", "info", "--format", "{{.ServerVersion}}"],
                    cwd=DATA.parent,
                    timeout=10,
                )
                if result.returncode:
                    failures.append("Docker is installed but its service is unavailable.")
                else:
                    print("Docker service is available.")
            except Exception:
                failures.append("Docker did not answer within the diagnostic time limit.")
    for failure in failures:
        print("Check: " + failure)
    print(
        "Environment ready."
        if not failures
        else "Resolve the checks above and run this command again."
    )
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
