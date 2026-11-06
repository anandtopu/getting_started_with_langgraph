"""Validate released tasks; --release requires the entire planned course."""

import argparse
import ast
import json
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

from common.loading import load_module
from common.optional import missing_for
from common.process import offline_environment, run_process
from gym.answers import read_hints
from gym.catalog import Catalog
from gym.runner import check_task


def validate(*, release: bool = False, identifier: str | None = None, jobs: int = 1) -> list[str]:
    catalog = Catalog()
    errors = []
    selected = [catalog.get(identifier)] if identifier else catalog.available()
    absent = [(task, missing_for(task.id)) for task in selected if missing_for(task.id)]
    if absent:
        for module, reason in sorted({(task.module, reason) for task, reason in absent}):
            print(f"SKIP {module}: {reason}", flush=True)
        if release or identifier:
            return [f"{task.id}: {reason}" for task, reason in absent]
        selected = [task for task in selected if not missing_for(task.id)]
    if jobs > 1 and identifier is None:
        with ThreadPoolExecutor(max_workers=jobs) as pool:
            results = list(pool.map(lambda task: validate(identifier=task.id), selected))
        errors = [error for result in results for error in result]
        if release:
            errors.extend(release_errors(catalog))
        print(f"Validated {len(selected)} released tasks using {jobs} bounded grader workers.")
        return errors
    if not selected:
        errors.append("No released tasks exist; an empty validation is not a pass.")
    for task in selected:
        print(f"Validating {task.id}...", flush=True)
        required = ["task.md", "test_task.py", "hints.md", "solution.py", "explanation.md"]
        required += ["answer.json", "expected_answer.json"] if task.answer_task else ["starter.py"]
        if task.type == "design":
            required += ["design.md", "solution_design.md", "rubric.md"]
        absent = [name for name in required if not (task.folder / name).is_file()]
        if absent:
            errors.append(f"{task.id}: missing {', '.join(absent)}")
            continue
        try:
            read_hints(task.folder / "hints.md")
            for name in ("task.md", "explanation.md"):
                if len((task.folder / name).read_text("utf-8").strip()) < 80:
                    errors.append(f"{task.id}: {name} is too short to explain the task.")
            for path in task.folder.glob("*.py"):
                tree = ast.parse(path.read_text("utf-8"), filename=str(path))
                if any(
                    isinstance(node, ast.Constant) and node.value is Ellipsis
                    for node in ast.walk(tree)
                ):
                    errors.append(f"{task.id}: executable file contains an ellipsis body.")
            solution = task.folder / ("expected_answer.json" if task.answer_task else "solution.py")
            solved = check_task(task, solution)
            if not solved.passed:
                errors.append(f"{task.id}: reference failed\n{solved.output}")
            if task.answer_task:
                oracle = load_module(task.folder / "solution.py").run()
                if oracle != json.loads(solution.read_text("utf-8")):
                    errors.append(f"{task.id}: committed answer differs from actual oracle output.")
            else:
                starter = check_task(task, task.folder / "starter.py")
                if (
                    starter.passed
                    or starter.returncode != 1
                    or task.expected_failure not in starter.output
                ):
                    errors.append(
                        f"{task.id}: starter did not fail for its declared behavioral reason\n{starter.output}"
                    )
                for name in ("starter.py", "solution.py"):
                    result = run_process(
                        [sys.executable, "-m", "common.offline", str(task.folder / name)],
                        cwd=catalog.root,
                        timeout=task.timeout,
                        env=offline_environment(),
                    )
                    if result.returncode:
                        errors.append(f"{task.id}: {name} does not run on its own\n{result.stdout}")
        except Exception as error:
            errors.append(f"{task.id}: {type(error).__name__}: {error}")
    if release:
        errors.extend(release_errors(catalog))
    print(
        f"Checked {len(selected)} released tasks; {len(catalog.available())}/{len(catalog.tasks)} planned tasks are available."
    )
    return errors


def release_errors(catalog: Catalog) -> list[str]:
    errors = []
    missing = [task.id for task in catalog.tasks.values() if not task.available]
    if missing:
        errors.append(f"Release incomplete: {len(missing)} planned tasks are not released.")
    if len(catalog.available()) < 140:
        errors.append("Release requires at least 140 tasks.")
    for module in sorted({task.module for task in catalog.tasks.values()}):
        tasks = [task for task in catalog.available() if task.module == module]
        if (
            len(tasks) < 6
            or len({task.type for task in tasks}) < 4
            or {task.level for task in tasks} != {"easy", "medium", "hard"}
        ):
            errors.append(f"{module}: release task distribution is incomplete.")
    groups = Counter(task.group for task in catalog.available())
    if any(groups[task.group] < 6 for task in catalog.tasks.values()):
        errors.append("Some feature groups do not yet have six released tasks.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--task")
    parser.add_argument("--jobs", type=int, default=4, choices=range(1, 9))
    arguments = parser.parse_args()
    errors = validate(release=arguments.release, identifier=arguments.task, jobs=arguments.jobs)
    for error in errors:
        print(error)
    print(
        "Gym validation passed for the released scope."
        if not errors
        else f"{len(errors)} validation problem(s)."
    )
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
