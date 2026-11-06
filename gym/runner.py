"""Grade the chosen file with offline pytest in a bounded child process."""

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from common.process import offline_environment, run_process
from gym.catalog import ROOT, Task


@dataclass(frozen=True)
class CheckResult:
    passed: bool
    returncode: int
    output: str
    tests: tuple[dict, ...] = ()
    timed_out: bool = False


def check_task(task: Task, candidate: Path, *, root: Path = ROOT) -> CheckResult:
    from common.optional import missing_for

    missing = missing_for(task.id)
    if missing:
        return CheckResult(False, 2, missing)
    if not candidate.is_file() or candidate.is_symlink():
        raise ValueError("No regular attempt file found. Start the task first.")
    with tempfile.TemporaryDirectory(prefix="larkspur-grade-") as temporary:
        report = Path(temporary) / "result.json"
        command = [
            sys.executable,
            "-m",
            "pytest",
            str(task.folder / "test_task.py"),
            "-c",
            str(root / "pyproject.toml"),
            "-q",
            "-p",
            "pytest_socket",
            "-p",
            "pytest_asyncio.plugin",
            "-p",
            "gym.pytest_plugin",
            "--candidate",
            str(candidate.resolve()),
            "--gym-report",
            str(report),
            "--basetemp",
            str(Path(temporary) / "pytest"),
        ]
        try:
            result = run_process(command, cwd=root, timeout=task.timeout, env=offline_environment())
        except subprocess.TimeoutExpired as error:
            return CheckResult(
                False,
                124,
                f"Time limit exceeded ({task.timeout:g}s). Check for a loop without an exit.\n{error.output or ''}",
                timed_out=True,
            )
        payload = json.loads(report.read_text("utf-8")) if report.exists() else {"tests": []}
    tests = tuple(payload["tests"])
    calls = [entry for entry in tests if entry["when"] == "call"]
    passed = (
        result.returncode == 0
        and bool(calls)
        and all(entry["outcome"] == "passed" for entry in tests)
    )
    if result.returncode == 0 and not passed:
        return CheckResult(
            False,
            5,
            "No complete set of checks ran; skipped tests do not count as a pass.\n"
            + result.stdout,
            tests,
        )
    return CheckResult(passed, result.returncode, result.stdout, tests)
