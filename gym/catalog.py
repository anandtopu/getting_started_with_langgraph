"""Catalog planned and released exercises without treating missing work as complete."""

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Task:
    id: str
    module: str
    type: str
    level: str
    description: str
    folder: Path
    group: str
    available: bool
    prerequisites: tuple[str, ...] = ()
    timeout: float = 30
    expected_failure: str = "LARKSPUR"
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def answer_task(self) -> bool:
        return self.type in {"predict", "trace"}

    def attempt_path(self, workspace: Path) -> Path:
        return workspace / (self.id + (".answer.json" if self.answer_task else ".py"))

    def copies(self, workspace: Path) -> list[tuple[Path, Path]]:
        primary = "answer.json" if self.answer_task else "starter.py"
        result = [(self.folder / primary, self.attempt_path(workspace))]
        if self.type == "design":
            result.append((self.folder / "design.md", workspace / (self.id + ".design.md")))
        if self.module == "B1" and not self.answer_task:
            result.append((self.folder / "starter.ts", workspace / (self.id + ".ts")))
        return result

    def attempt_files(self, workspace: Path) -> list[Path]:
        return [target for _, target in self.copies(workspace)]


class Catalog:
    def __init__(self, root: Path = ROOT):
        self.root = root.resolve()
        source = json.loads((self.root / "docs/planning/course_catalog.json").read_text("utf-8"))
        released = json.loads((self.root / "gym/manifest.json").read_text("utf-8"))
        if released.get("schema_version") != 1:
            raise ValueError("Unsupported gym manifest version.")
        self.phase = released["phase"]
        self.milestones = released.get("milestones", {})
        self.tasks: dict[str, Task] = {}
        for module in source["modules"]:
            for group in module["groups"]:
                for row in group["tasks"]:
                    identifier = row["id"]
                    if (
                        not re.fullmatch(r"(?:\d{2}|B[1-4])-\d{2}", identifier)
                        or identifier in self.tasks
                    ):
                        raise ValueError("Invalid or repeated task ID in the catalog.")
                    folder = (self.root / row["folder"]).resolve()
                    if not folder.is_relative_to(self.root / "gym/tasks"):
                        raise ValueError("A task folder escapes gym/tasks/.")
                    entry = released["tasks"].get(identifier)
                    self.tasks[identifier] = Task(
                        id=identifier,
                        module=row["module"],
                        type=row["type"],
                        level=row["level"],
                        description=row["description"],
                        folder=folder,
                        group=group["id"],
                        available=entry is not None,
                        prerequisites=tuple(entry.get("prerequisites", [])) if entry else (),
                        timeout=float(entry.get("timeout", 30)) if entry else 30,
                        expected_failure=entry.get("expected_failure", "LARKSPUR") if entry else "",
                        metadata=entry or {},
                    )
        unknown = set(released["tasks"]) - self.tasks.keys()
        if unknown:
            raise ValueError("The gym manifest contains IDs missing from the course catalog.")
        for task in self.tasks.values():
            if any(item not in self.tasks for item in task.prerequisites):
                raise ValueError(f"Unknown prerequisite for {task.id}.")

    def get(self, identifier: str, *, require_available: bool = True) -> Task:
        task = self.tasks.get(identifier)
        if task is None:
            raise ValueError("Unknown task ID. Use: gym list")
        if require_available and not task.available:
            raise ValueError(f"{identifier} is planned for a later phase; it is not released yet.")
        return task

    def available(self) -> list[Task]:
        return [task for task in self.tasks.values() if task.available]
