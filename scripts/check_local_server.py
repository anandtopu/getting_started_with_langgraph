"""Verify SQLite pause/restart/resume through a real owned loopback server process."""

import os
import secrets
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import httpx

from common.config import ROOT
from common.effects import EffectLedger
from common.process import offline_environment, run_process


def main():
    with socket.socket() as reserved:
        reserved.bind(("127.0.0.1", 0))
        port = reserved.getsockname()[1]
    url = f"http://127.0.0.1:{port}"
    with tempfile.TemporaryDirectory(prefix="larkspur-server-") as temporary:
        directory = Path(temporary)
        environment = offline_environment()
        environment.pop("DATABASE_URL", None)
        environment.update(
            LARKSPUR_STATE_DIR=str(directory / "state"),
            LARKSPUR_CUSTOMER_TOKEN=secrets.token_hex(24),
            LARKSPUR_ADJUSTER_TOKEN=secrets.token_hex(24),
        )
        for stage in ("start", "resume"):
            with (directory / "server.log").open("a", encoding="utf-8") as log:
                process = subprocess.Popen(
                    [
                        sys.executable,
                        "-m",
                        "uvicorn",
                        "apps.server:build_app",
                        "--factory",
                        "--host",
                        "127.0.0.1",
                        "--port",
                        str(port),
                    ],
                    cwd=ROOT,
                    env=environment,
                    stdout=log,
                    stderr=subprocess.STDOUT,
                    creationflags=(
                        subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP
                    )
                    if os.name == "nt"
                    else 0,
                )
                try:
                    deadline = time.monotonic() + 30
                    while time.monotonic() < deadline:
                        if process.poll() is not None:
                            raise RuntimeError("Owned API process stopped before readiness")
                        try:
                            if httpx.get(url + "/health", timeout=1).status_code == 200:
                                break
                        except httpx.RequestError:
                            pass
                        time.sleep(0.1)
                    else:
                        raise TimeoutError("Owned API process did not become ready")
                    result = run_process(
                        [
                            sys.executable,
                            "scripts/check_deployment.py",
                            stage,
                            "--base-url",
                            url,
                            "--state-file",
                            str(directory / "thread.json"),
                        ],
                        cwd=ROOT,
                        env=environment,
                        timeout=180,
                    )
                    if result.returncode:
                        raise RuntimeError(result.stdout)
                finally:
                    if process.poll() is None:
                        if os.name == "nt":
                            # A Windows virtualenv launcher can own a separate interpreter process.
                            subprocess.run(
                                ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL,
                                check=False,
                                creationflags=subprocess.CREATE_NO_WINDOW,
                                timeout=10,
                            )
                        else:
                            process.terminate()
                        try:
                            process.wait(timeout=10)
                        except subprocess.TimeoutExpired:
                            process.kill()
                            process.wait(timeout=5)
                    deadline = time.monotonic() + 10
                    while time.monotonic() < deadline:
                        with socket.socket() as probe:
                            probe.settimeout(0.2)
                            if probe.connect_ex(("127.0.0.1", port)) != 0:
                                break
                        time.sleep(0.1)
                    else:
                        raise RuntimeError(
                            "The owned server did not release its port before restart"
                        )
        assert len(EffectLedger(directory / "state/ownership.db").rows()) == 1
    print(
        "PASS real local API restart, durable approval, role checks, stale decision, and one effect"
    )


if __name__ == "__main__":
    main()
