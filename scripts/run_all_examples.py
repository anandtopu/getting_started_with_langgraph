"""Smoke-test shipped examples offline; live model variants require explicit --live."""

import argparse
import ast
import os
import sys
from pathlib import Path

from common.data import ROOT
from common.optional import missing_for_path
from common.process import offline_environment, run_process


def examples() -> list[Path]:
    paths = [ROOT / "scripts/first_graph.py", ROOT / "scripts/fake_model_demo.py"]
    paths.extend(sorted((ROOT / "modules").glob("**/examples/*.py")))
    paths.extend(sorted((ROOT / "modules").glob("**/use_case/*.py")))
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true")
    arguments = parser.parse_args()
    failures = 0
    checked = 0
    skipped = 0
    for path in examples():
        missing = missing_for_path(path)
        if missing:
            print(f"SKIP {path.relative_to(ROOT)}: {missing}")
            skipped += 1
            continue
        checked += 1
        docstring = ast.get_docstring(ast.parse(path.read_text("utf-8"))) or ""
        use_live = arguments.live and "LLM: optional" in docstring
        command = [sys.executable] + ([] if use_live else ["-m", "common.offline"]) + [str(path)]
        if use_live:
            command.append("--live")
        try:
            result = run_process(
                command,
                cwd=ROOT,
                timeout=120 if use_live else 30,
                env=dict(os.environ) if use_live else offline_environment(),
            )
            if result.returncode:
                failures += 1
                print(result.stdout)
            print(
                f"{'PASS' if result.returncode == 0 else 'FAIL'} {path.relative_to(ROOT)}",
                flush=True,
            )
        except Exception as error:
            failures += 1
            print(f"FAIL {path.relative_to(ROOT)}: {type(error).__name__}")
    print(f"{checked} shipped examples checked; {skipped} optional examples skipped.")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
