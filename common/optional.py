"""Explicit installation requirements for optional course lessons."""

import importlib.util
import shutil
from pathlib import Path

REQUIREMENTS = {
    "16": [("mcp", "mcp"), ("langchain_mcp_adapters", "mcp")],
    "18": [("fastapi", "apps")],
    "19": [("agentevals", "eval")],
    "21": [("fastapi", "apps"), ("Crypto", "security")],
    "22": [("fastapi", "apps")],
    "B2": [("deepagents", "bonus")],
}


def missing_for(identifier: str) -> str | None:
    module = identifier.split("-")[0]
    missing = sorted(
        {
            extra
            for package, extra in REQUIREMENTS.get(module, [])
            if importlib.util.find_spec(package) is None
        }
    )
    if missing:
        return "Install this lesson with uv sync " + " ".join("--extra " + name for name in missing)
    if module == "B1":
        root = Path(__file__).resolve().parents[1]
        if not shutil.which("node") or not (root / "node_modules/@langchain/langgraph").exists():
            return "Install Node.js 24 and run npm ci for the TypeScript bonus."
    return None


def missing_for_path(path: Path) -> str | None:
    for part in path.parts:
        prefix = part.split("_")[0]
        if prefix in REQUIREMENTS or prefix == "B1":
            return missing_for(prefix)
    return None
