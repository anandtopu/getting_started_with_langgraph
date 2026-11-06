"""Grade one capstone against a selected learner file, offline."""

import argparse
import sys
from pathlib import Path

from common.config import ROOT
from common.process import offline_environment, run_process


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("number", choices=["01", "02", "03", "04", "05"])
    parser.add_argument("--candidate", type=Path, required=True)
    args = parser.parse_args()
    folder = next((ROOT / "capstones").glob(args.number + "_*"))
    environment = offline_environment()
    environment["LARKSPUR_CAPSTONE_FILE"] = str(args.candidate.resolve())
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
        ],
        cwd=ROOT,
        env=environment,
        timeout=180,
    )
    print(result.stdout)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
