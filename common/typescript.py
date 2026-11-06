"""Run a TypeScript learner file in Node 24; the Python wrapper never supplies its answer."""

import json
import shutil
from pathlib import Path

from common.config import ROOT
from common.process import offline_environment, run_process


class TypeScriptError(RuntimeError):
    """The JavaScript program reported a rejected input or graph execution error."""


def run_typescript(path: Path, case: dict) -> dict:
    node = shutil.which("node")
    if node is None or not (ROOT / "node_modules/@langchain/langgraph").exists():
        raise RuntimeError("Install Node 24 and run npm ci before the optional B1 exercises")
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
