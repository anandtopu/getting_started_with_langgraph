"""Bounded child processes with portable cleanup and secret-free grading environments."""

import os
import signal
import subprocess
from collections.abc import Sequence
from contextlib import suppress
from pathlib import Path


def offline_environment() -> dict[str, str]:
    environment = {
        key: value
        for key, value in os.environ.items()
        if not any(word in key.upper() for word in ("KEY", "TOKEN", "SECRET", "PASSWORD"))
    }
    environment.update(
        LANGSMITH_TRACING="false",
        LANGCHAIN_TRACING_V2="false",
        LARKSPUR_OFFLINE="1",
        PYTHONUTF8="1",
        PYTHONIOENCODING="utf-8",
        PYTEST_DISABLE_PLUGIN_AUTOLOAD="1",
    )
    return environment


def run_process(
    command: Sequence[str],
    *,
    cwd: Path,
    timeout: float = 30,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    flags = (
        subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0
    )
    process = subprocess.Popen(
        list(command),
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        creationflags=flags,
        start_new_session=os.name != "nt",
    )
    try:
        output, _ = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        if os.name == "nt":
            with suppress(OSError, subprocess.TimeoutExpired):
                subprocess.run(
                    ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=False,
                    creationflags=subprocess.CREATE_NO_WINDOW,
                    timeout=5,
                )
            # The owned process handle remains usable even when taskkill is restricted.
            process.kill()
        else:
            os.killpg(process.pid, signal.SIGKILL)
        try:
            output, _ = process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            if process.stdout is not None:
                process.stdout.close()
            output = "The grader exceeded its deadline; child output was closed."
        raise subprocess.TimeoutExpired(list(command), timeout, output=output) from None
    return subprocess.CompletedProcess(list(command), process.returncode, output, "")
