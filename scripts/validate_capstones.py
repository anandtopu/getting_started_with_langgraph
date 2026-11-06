"""Prove each capstone reference passes and each runnable starter fails behaviorally."""

import sys

from common.config import ROOT
from common.process import offline_environment, run_process


def main():
    for folder in sorted((ROOT / "capstones").glob("[0-9][0-9]_*")):
        for name, expected_code in (("solution.py", 0), ("starter.py", 1)):
            result = run_process(
                [
                    sys.executable,
                    "scripts/check_capstone.py",
                    folder.name[:2],
                    "--candidate",
                    str(folder / name),
                ],
                cwd=ROOT,
                env=offline_environment(),
                timeout=180,
            )
            assert result.returncode == expected_code, (folder.name, name, result.stdout)
            if expected_code:
                assert "CAPSTONE:" in result.stdout, (folder.name, result.stdout)
            standalone = run_process(
                [sys.executable, "-m", "common.offline", str(folder / name)],
                cwd=ROOT,
                env=offline_environment(),
                timeout=120,
            )
            assert standalone.returncode == 0, (folder.name, standalone.stdout)
        print("PASS", folder.name, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
