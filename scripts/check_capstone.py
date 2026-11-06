"""Grade one capstone against a selected learner file, offline."""

import argparse
import json
import sys
import tempfile
from pathlib import Path

from common.config import ROOT
from common.process import offline_environment, run_process


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("number", choices=["01", "02", "03", "04", "05"])
    parser.add_argument("--candidate", type=Path, required=True)
    args = parser.parse_args()
    if not args.candidate.is_file() or args.candidate.is_symlink():
        parser.error("Choose a regular candidate Python file")
    folder = next((ROOT / "capstones").glob(args.number + "_*"))
    environment = offline_environment()
    environment["LARKSPUR_CAPSTONE_FILE"] = str(args.candidate.resolve())
    with tempfile.TemporaryDirectory(prefix="larkspur-capstone-") as directory:
        report = Path(directory) / "result.json"
        result = run_process(
            [
                sys.executable,
                "-m",
                "pytest",
                str(folder / "tests"),
                "-q",
                "-p",
                "pytest_socket",
                "-p",
                "pytest_asyncio.plugin",
                "-p",
                "gym.pytest_plugin",
                "--candidate",
                str(args.candidate.resolve()),
                "--gym-report",
                str(report),
            ],
            cwd=ROOT,
            env=environment,
            timeout=180,
        )
        tests = json.loads(report.read_text("utf-8"))["tests"] if report.exists() else []
    print(result.stdout)
    if result.returncode == 0 and (
        not any(row["when"] == "call" for row in tests)
        or any(row["outcome"] != "passed" for row in tests)
    ):
        print("No complete acceptance set ran; skipped tests do not count as a capstone pass.")
        return 5
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
