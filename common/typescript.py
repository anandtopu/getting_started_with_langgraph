"""Run a TypeScript learner file in Node 24; the Python wrapper never supplies its answer."""

import json
import shutil
import tempfile
from pathlib import Path

from common.config import ROOT
from common.process import offline_environment, run_process


class TypeScriptError(RuntimeError):
    """The JavaScript program reported a rejected input or graph execution error."""


def run_typescript(path: Path, case: dict) -> dict:
    node = shutil.which("node")
    if node is None or not (ROOT / "node_modules/@langchain/langgraph").exists():
        raise RuntimeError("Install Node 24 and run npm ci before the optional B1 exercises")
    if not path.resolve().is_relative_to(ROOT):
        # Node resolves ESM packages from the script location, not cwd. An external
        # --workspace still grades the exact selected single-file TS attempt.
        staging = ROOT / "tmp"
        staging.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="typescript-attempt-", dir=staging) as directory:
            selected = Path(directory) / "attempt.ts"
            shutil.copyfile(path, selected)
            return run_typescript(selected, case)
    result = run_process(
        [
            node,
            "--import",
            (ROOT / "common/node_offline.mjs").as_uri(),
            str(path.resolve()),
            json.dumps(case),
        ],
        cwd=ROOT,
        timeout=30,
        env=offline_environment(),
    )
    if result.returncode:
        raise TypeScriptError("TypeScript did not execute; inspect the selected .ts file")
    response = json.loads(result.stdout.strip().splitlines()[-1])
    if "error" in response:
        raise TypeScriptError(response["error"])
    return response["value"]
