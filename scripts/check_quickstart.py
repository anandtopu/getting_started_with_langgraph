"""Time an automated first-task repair in a fresh local clone of committed files."""

import argparse
import json
import tempfile
import time
from pathlib import Path

from common.config import ROOT
from common.process import offline_environment, run_process


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--offline-install", action="store_true", help="Require a warm uv package cache."
    )
    arguments = parser.parse_args()
    temporary = ROOT / "tmp"
    temporary.mkdir(exist_ok=True)
    clone = Path(tempfile.mkdtemp(prefix="quickstart-", dir=temporary))
    environment = offline_environment()
    started = time.perf_counter()
    stages = []

    def run(label: str, command: list[str], expected: int = 0) -> None:
        result = run_process(command, cwd=clone, timeout=180, env=environment)
        if result.returncode != expected:
            raise RuntimeError(f"{label} failed:\n{result.stdout}")
        stages.append(label)
        print(f"PASS {label}", flush=True)

    run("fresh local clone", ["git", "clone", "--local", str(ROOT), str(clone)])
    install = ["uv", "sync", "--locked"]
    if arguments.offline_install:
        install.append("--offline")
    run("base installation", install)
    run("environment check", ["uv", "run", "--no-sync", "python", "scripts/check_env.py"])
    run("first graph", ["uv", "run", "--no-sync", "python", "scripts/first_graph.py"])
    run("first task", ["uv", "run", "--no-sync", "gym", "start", "00-01"])
    run("intentional starter failure", ["uv", "run", "--no-sync", "gym", "check", "00-01"], 1)
    # Apply the two conditions explained by the first exercise. This is an
    # automated repair benchmark, not a measurement of a novice learning time.
    attempt = clone / "workspace/00-01.py"
    source = attempt.read_text("utf-8")
    assert "if False:" in source and "elif False:" in source
    source = source.replace("    if False:", '    if normalized.get("duplicate_of"):')
    source = source.replace("elif False:", "elif missing:")
    attempt.write_text(source, encoding="utf-8")
    run("repaired task passes", ["uv", "run", "--no-sync", "gym", "check", "00-01"])
    report = {
        "kind": "automated guided repair; not a novice usability study",
        "seconds": round(time.perf_counter() - started, 2),
        "offline_install": arguments.offline_install,
        "stages": stages,
    }
    (temporary / "quickstart-result.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    print(f"Inspection clone retained at {clone}")


if __name__ == "__main__":
    main()
