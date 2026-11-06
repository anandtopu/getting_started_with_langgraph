"""Portable Practice Gym commands. Run: uv run gym --help."""

import argparse
import random
import shutil
import sys
import uuid
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from gym.answers import read_hints
from gym.catalog import ROOT, Catalog, Task
from gym.progress import ProgressStore, fingerprint, is_current_pass, timestamp
from gym.runner import check_task


def confirm(message: str, yes: bool) -> bool:
    if yes:
        return True
    try:
        return input(message + " [y/N] ").strip().lower() in {"y", "yes"}
    except EOFError:
        return False


def copy_attempt(task: Task, workspace: Path, *, replace: bool = False) -> Path:
    pairs = task.copies(workspace)
    workspace.mkdir(parents=True, exist_ok=True)
    for source, target in pairs:
        if not source.is_file():
            raise ValueError(f"The released task is missing {source.name}; report a content error.")
        if target.is_symlink():
            raise ValueError("Refusing to overwrite a symlink in the workspace.")
        if target.exists() and not replace:
            raise ValueError(f"Attempt already exists: {target.name}. Use gym reset to replace it.")
    for source, target in pairs:
        shutil.copyfile(source, target)
    return task.attempt_path(workspace)


def completed_modules(catalog: Catalog, workspace: Path, data: dict[str, Any]) -> set[str]:
    completed = set()
    for module, identifiers in catalog.milestones.items():
        if identifiers and all(
            identifier in catalog.tasks
            and catalog.tasks[identifier].available
            and is_current_pass(
                catalog.tasks[identifier], workspace, data["tasks"].get(identifier, {})
            )
            for identifier in identifiers
        ):
            completed.add(module)
    return completed


def show_progress(catalog: Catalog, workspace: Path, data: dict[str, Any]) -> None:
    counts = defaultdict(Counter)
    types = defaultdict(Counter)
    for task in catalog.tasks.values():
        counts[task.module]["planned"] += 1
        if not task.available:
            continue
        row = data["tasks"].get(task.id, {})
        counts[task.module]["available"] += 1
        types[task.type]["available"] += 1
        if fingerprint(task, workspace):
            counts[task.module]["started"] += 1
        if row.get("solution_viewed"):
            counts[task.module]["solution_viewed"] += 1
        if row.get("hints", 0):
            counts[task.module]["hinted"] += 1
        if is_current_pass(task, workspace, row):
            counts[task.module]["passed"] += 1
            types[task.type]["passed"] += 1
        if is_current_pass(task, workspace, row, independent=True):
            counts[task.module]["independent"] += 1
        if row.get("passed") and row.get("attempt_hash") != fingerprint(task, workspace):
            counts[task.module]["stale"] += 1
    done = completed_modules(catalog, workspace, data)
    print(
        f"Phase {catalog.phase} progress (passing an assisted attempt is separate from an independent pass)"
    )
    print("Module  Available/planned  Passed  Independent  Stale  Milestone")
    for module, row in sorted(counts.items()):
        print(
            f"{module:6}  {row['available']:3}/{row['planned']:<3}          {row['passed']:3}     {row['independent']:3}          {row['stale']:3}    {'complete' if module in done else 'pending'}"
        )
        if row["available"]:
            print(
                f"        Started: {row['started']}; hints used: {row['hinted']}; "
                f"solutions viewed: {row['solution_viewed']}; "
                f"full mastery: {'complete' if row['passed'] == row['planned'] else 'pending'}"
            )
    print("\nBy task type:")
    for kind, row in sorted(types.items()):
        print(f"  {kind}: {row['passed']}/{row['available']} current passes")
    print(
        "Design passes include a declared self-review; they are not an automated quality certification."
    )


def recommend(catalog: Catalog, workspace: Path, data: dict[str, Any]) -> Task | None:
    eligible = []
    milestone_ids = {item for identifiers in catalog.milestones.values() for item in identifiers}
    for task in catalog.available():
        if is_current_pass(task, workspace, data["tasks"].get(task.id, {})):
            continue
        if all(
            is_current_pass(catalog.tasks[item], workspace, data["tasks"].get(item, {}))
            for item in task.prerequisites
        ):
            eligible.append(task)
    return (
        min(eligible, key=lambda task: (task.id not in milestone_ids, task.id))
        if eligible
        else None
    )


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Practice LangGraph offline with fictional Larkspur claims."
    )
    parser.add_argument("--workspace", type=Path, default=ROOT / "workspace")
    subcommands = parser.add_subparsers(dest="command", required=True)
    for name in (
        "list",
        "start",
        "check",
        "hint",
        "solution",
        "reset",
        "progress",
        "next",
        "drill",
    ):
        sub = subcommands.add_parser(name)
        sub.add_argument("--workspace", type=Path, default=argparse.SUPPRESS)
        if name in {"start", "check", "hint", "solution", "reset"}:
            sub.add_argument("task_id")
        if name == "list":
            sub.add_argument("--module")
            sub.add_argument(
                "--type",
                choices=["build", "fix", "predict", "trace", "refactor", "extend", "design"],
            )
            sub.add_argument("--level", choices=["easy", "medium", "hard"])
            sub.add_argument("--available", action="store_true")
        if name in {"solution", "reset"}:
            sub.add_argument(
                "--yes",
                action="store_true",
                help="Explicitly confirm without an interactive prompt.",
            )
        if name == "check":
            sub.add_argument(
                "--self-reviewed",
                action="store_true",
                help="Declare completion of the Design rubric.",
            )
            sub.add_argument(
                "--attempt",
                type=Path,
                help="Grade an isolated drill attempt, without updating the normal attempt.",
            )
        if name == "drill":
            sub.add_argument("--seed", type=int)
    return parser


def execute(arguments: argparse.Namespace, catalog: Catalog) -> int:
    if arguments.command == "list":
        selected = [
            task
            for task in catalog.tasks.values()
            if (not arguments.module or task.module == arguments.module.upper().zfill(2))
            and (not arguments.type or task.type == arguments.type)
            and (not arguments.level or task.level == arguments.level)
            and (not arguments.available or task.available)
        ]
        print("ID     Module Type      Level   Status     Description")
        milestones = {item for identifiers in catalog.milestones.values() for item in identifiers}
        for task in selected:
            print(
                f"{task.id:6} {task.module:6} {task.type:9} {task.level:7} {'available' if task.available else 'planned':10} {task.description}"
            )
            if task.available:
                print(
                    f"       Prerequisites: {', '.join(task.prerequisites) or 'none'}; "
                    f"guided milestone: {'yes' if task.id in milestones else 'no'}"
                )
        print(
            f"{len(selected)} matching tasks; {len(catalog.available())} available of {len(catalog.tasks)} planned."
        )
        return 0

    workspace = arguments.workspace.resolve()
    store = ProgressStore(workspace)
    data = store.read()
    if store.recovery_message:
        print(store.recovery_message)
    if arguments.command == "progress":
        show_progress(catalog, workspace, data)
        return 0
    if arguments.command == "next":
        task = recommend(catalog, workspace, data)
        if task:
            print(f"Next: {task.id} ({task.type}, {task.level}) — {task.description}")
            print(f"uv run gym start {task.id}")
        else:
            print(
                "No eligible unfinished task is available. Finish prerequisite reviews or return when the next phase is released."
            )
        return 0
    if arguments.command == "drill":
        finished = completed_modules(catalog, workspace, data)
        choices = [
            task
            for task in catalog.available()
            if task.module in finished and task.type in {"predict", "fix"}
        ]
        if not choices:
            print("Finish one module's available milestone before a drill. Use gym next to begin.")
            return 0
        history = data["drills"]
        weights = [
            1
            + sum(
                item.get("task_id") == task.id and item.get("passed") is False for item in history
            )
            for task in choices
        ]
        task = random.Random(arguments.seed).choices(choices, weights=weights, k=1)[0]
        directory = workspace / ".drills" / uuid.uuid4().hex
        attempt = copy_attempt(task, directory)
        with store.transaction() as progress:
            progress["drills"].append(
                {"task_id": task.id, "attempt": str(attempt), "started_at": timestamp()}
            )
        print(f"Drill: {task.id}\n{(task.folder / 'task.md').read_text('utf-8')}")
        print(f'Check this isolated attempt: uv run gym check {task.id} --attempt "{attempt}"')
        return 0

    task = catalog.get(arguments.task_id)
    if arguments.command == "start":
        attempt = copy_attempt(task, workspace)
        store.update(task.id, started_at=timestamp())
        print((task.folder / "task.md").read_text("utf-8"))
        print(f"Edit: {attempt}\nCheck: uv run gym check {task.id}")
        return 0
    if arguments.command == "hint":
        hints = read_hints(task.folder / "hints.md")
        index = store.next_hint(task.id)
        print(
            hints[index]
            if index < 3
            else "All three hints have been revealed. Review them in the task folder or request the solution."
        )
        return 0
    if arguments.command == "solution":
        if not confirm(
            "Reveal the reference solution? This is recorded as assisted study.", arguments.yes
        ):
            print("Solution not revealed.")
            return 0
        store.update(task.id, solution_viewed=True)
        for name in ("expected_answer.json",) if task.answer_task else ("solution.py",):
            print((task.folder / name).read_text("utf-8"))
        if task.type == "design":
            print((task.folder / "solution_design.md").read_text("utf-8"))
        print((task.folder / "explanation.md").read_text("utf-8"))
        return 0
    if arguments.command == "reset":
        if not confirm("Back up this attempt and reset it to the starter?", arguments.yes):
            print("Attempt unchanged.")
            return 0
        pairs = task.copies(workspace)
        if any(target.is_symlink() for _, target in pairs):
            raise ValueError("Refusing to reset a symlink.")
        backup = workspace / ".backups" / (task.id + "-" + uuid.uuid4().hex)
        backup.mkdir(parents=True)
        for _, target in pairs:
            if target.exists():
                shutil.copyfile(target, backup / target.name)
        copy_attempt(task, workspace, replace=True)
        store.reset(task.id)
        print(f"Reset {task.id}. Previous files: {backup}")
        return 0
    if arguments.command == "check":
        attempt = arguments.attempt.resolve() if arguments.attempt else task.attempt_path(workspace)
        if arguments.attempt and not attempt.is_relative_to(workspace / ".drills"):
            raise ValueError(
                "Alternate attempts must be generated under this workspace's .drills folder."
            )
        if arguments.attempt and not any(
            item["attempt"] == str(attempt) and item["task_id"] == task.id
            for item in data["drills"]
        ):
            raise ValueError("This drill attempt is not recorded in this workspace.")
        digest = fingerprint(task, attempt.parent)
        if digest is None:
            raise ValueError(
                "The attempt or a required companion file is missing. Use gym start first."
            )
        result = check_task(task, attempt, root=catalog.root)
        print(result.output.rstrip())
        if arguments.attempt:
            with store.transaction() as progress:
                matches = [
                    item
                    for item in progress["drills"]
                    if item["attempt"] == str(attempt) and item["task_id"] == task.id
                ]
                if not matches:
                    raise ValueError("This drill attempt is not recorded in this workspace.")
                matches[-1].update(passed=result.passed, checked_at=timestamp())
        else:
            store.record_check(task, digest, result.passed, reviewed=arguments.self_reviewed)
        print(
            "PASS"
            if result.passed
            else f"NOT YET — inspect the failure, then try: gym hint {task.id}"
        )
        if result.passed and task.type == "design" and not arguments.self_reviewed:
            print(
                f"Mechanical checks passed; rubric review pending. After self-review: gym check {task.id} --self-reviewed"
            )
        return 0 if result.passed else 1
    raise ValueError("Unsupported gym command.")


def main(argv: list[str] | None = None) -> int:
    arguments = make_parser().parse_args(argv)
    try:
        return execute(arguments, Catalog())
    except (ValueError, OSError, RuntimeError, TimeoutError) as error:
        print(f"Gym: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
