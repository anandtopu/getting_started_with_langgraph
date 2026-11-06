"""Refresh checked-in module overview diagrams from executable builders."""

import ast
import importlib
import json
import shutil
import tempfile

from common.config import ROOT
from common.process import offline_environment, run_process


def overview(module):
    folder = ROOT / module["path"]
    examples = sorted((folder / "examples").glob("*.mmd"))
    if examples:
        return examples[0].read_text("utf-8")
    if module["id"].isdigit():
        copilot = importlib.import_module(f"common.copilot.v{module['copilot_version']:02d}")
        return copilot.build_graph().get_graph(xray=True).draw_mermaid()
    if module["id"] == "B1":
        source = (folder / "examples/01_typescript_state.ts").read_text("utf-8")
        source = source.replace(
            "return await graph.invoke({ ...input, audit: [] });",
            "return graph.getGraph().drawMermaid();",
        )
        temporary_root = ROOT / "tmp"
        temporary_root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary_root) as directory:
            from pathlib import Path

            path = Path(directory) / "diagram.ts"
            path.write_text(source, encoding="utf-8")
            result = run_process(
                [shutil.which("node"), str(path)], cwd=ROOT, env=offline_environment()
            )
            if result.returncode:
                raise RuntimeError(result.stdout)
            return json.loads(result.stdout.strip().splitlines()[-1])["value"]
    leaf = "01_deep_agent_planning.py" if module["id"] == "B2" else "02_mini_reducers.py"
    path = folder / "examples" / leaf
    tree = ast.parse(path.read_text("utf-8"))
    function = next(
        node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "run"
    )
    name = "agent" if module["id"] == "B2" else "observed"
    index = next(
        index
        for index, node in enumerate(function.body)
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == name for target in node.targets)
    )
    end = index + 1 if module["id"] == "B2" else index
    expression = (
        "agent.get_graph().draw_mermaid()"
        if module["id"] == "B2"
        else "graph.compile().get_graph().draw_mermaid()"
    )
    function.body = function.body[:end] + ast.parse("return " + expression).body
    namespace = {"__name__": "course_diagram"}
    exec(compile(ast.fix_missing_locations(tree), str(path), "exec"), namespace)
    return namespace["run"]()


def main():
    catalog = json.loads((ROOT / "docs/planning/course_catalog.json").read_text("utf-8"))
    for module in catalog["modules"]:
        (ROOT / module["path"] / "diagram.mmd").write_text(
            overview(module).rstrip() + "\n", encoding="utf-8", newline="\n"
        )
    print("Refreshed all 27 module overview diagrams. Rebuild lesson docs to embed them.")


if __name__ == "__main__":
    main()
