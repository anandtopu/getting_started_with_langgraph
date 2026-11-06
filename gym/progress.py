"""Atomic progress updates with cross-process file locking and corruption recovery."""

import hashlib
import json
import os
import tempfile
import time
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from gym.catalog import Task


def timestamp() -> str:
    return datetime.now(UTC).isoformat()


def fingerprint(task: Task, workspace: Path) -> str | None:
    paths = task.attempt_files(workspace)
    if any(not path.is_file() or path.is_symlink() for path in paths):
        return None
    digest = hashlib.sha256()
    for path in paths:
        digest.update(path.name.encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


@contextmanager
def file_lock(path: Path, timeout: float = 5) -> Iterator[None]:
    if path.is_symlink():
        raise ValueError("Refusing a symlink for the progress lock.")
    with path.open("a+b") as handle:
        handle.seek(0, 2)
        if handle.tell() == 0:
            handle.write(b"0")
            handle.flush()
        end = time.monotonic() + timeout
        while True:
            handle.seek(0)
            try:
                if os.name == "nt":
                    import msvcrt

                    msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl

                    fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError:
                if time.monotonic() >= end:
                    raise TimeoutError(
                        "Progress is busy in another gym process; try again."
                    ) from None
                time.sleep(0.02)
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == "nt":
                import msvcrt

                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl

                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


class ProgressStore:
    def __init__(self, workspace: Path):
        self.workspace = workspace.resolve()
        self.workspace.mkdir(parents=True, exist_ok=True)
        self.path = self.workspace / ".progress.json"
        self.recovery_message: str | None = None

    def _read(self) -> dict[str, Any]:
        if self.path.is_symlink():
            raise ValueError("Refusing a symlink for the progress file.")
        if not self.path.exists():
            return {"schema_version": 1, "tasks": {}, "drills": []}
        try:
            data = json.loads(self.path.read_text("utf-8"))
            if not isinstance(data, dict) or not isinstance(data.get("tasks"), dict):
                raise ValueError("Malformed progress.")
            if data.get("schema_version") != 1:
                raise RuntimeError(
                    "Progress uses an unsupported version; keep the file and upgrade the gym."
                )
            if not isinstance(data.get("drills"), list):
                raise ValueError("Malformed drill history.")
            if any(not isinstance(value, dict) for value in data["tasks"].values()):
                raise ValueError("Malformed task progress.")
            for row in data["tasks"].values():
                for key in ("hints", "checks", "resets"):
                    if key in row and (type(row[key]) is not int or row[key] < 0):
                        raise ValueError("Malformed progress counter.")
                for key in ("passed", "reviewed", "independent", "solution_viewed"):
                    if key in row and type(row[key]) is not bool:
                        raise ValueError("Malformed progress flag.")
            for row in data["drills"]:
                if not isinstance(row, dict) or not all(
                    isinstance(row.get(key), str) for key in ("task_id", "attempt")
                ):
                    raise ValueError("Malformed drill entry.")
            return data
        except (ValueError, UnicodeError):
            backup = self.workspace / (".progress.corrupt-" + uuid.uuid4().hex + ".json")
            os.replace(self.path, backup)
            self.recovery_message = f"Recovered malformed progress; preserved it as {backup.name}."
            return {"schema_version": 1, "tasks": {}, "drills": []}

    def _write(self, data: dict[str, Any]) -> None:
        handle, temporary = tempfile.mkstemp(
            prefix=".progress-", suffix=".json", dir=self.workspace
        )
        try:
            with os.fdopen(handle, "w", encoding="utf-8") as output:
                json.dump(data, output, indent=2, sort_keys=True)
                output.write("\n")
                output.flush()
                os.fsync(output.fileno())
            os.replace(temporary, self.path)
        finally:
            Path(temporary).unlink(missing_ok=True)

    @contextmanager
    def transaction(self) -> Iterator[dict[str, Any]]:
        with file_lock(self.workspace / ".progress.lock"):
            data = self._read()
            yield data
            self._write(data)

    def read(self) -> dict[str, Any]:
        with self.transaction() as data:
            return json.loads(json.dumps(data))

    def update(self, identifier: str, **changes: Any) -> None:
        with self.transaction() as data:
            row = data["tasks"].setdefault(identifier, {})
            row.update(changes)
            row["updated_at"] = timestamp()

    def next_hint(self, identifier: str) -> int:
        with self.transaction() as data:
            row = data["tasks"].setdefault(identifier, {})
            count = min(max(int(row.get("hints", 0)), 0), 3)
            row["hints"] = min(count + 1, 3)
            row["updated_at"] = timestamp()
            return count

    def record_check(
        self, task: Task, digest: str, passed: bool, *, reviewed: bool = False
    ) -> None:
        with self.transaction() as data:
            row = data["tasks"].setdefault(task.id, {})
            row["checks"] = row.get("checks", 0) + 1
            row["passed"] = passed
            row["attempt_hash"] = digest
            row["independent"] = passed and not row.get("solution_viewed", False)
            row["reviewed"] = reviewed if task.type == "design" else True
            row["updated_at"] = timestamp()

    def reset(self, identifier: str) -> None:
        with self.transaction() as data:
            old = data["tasks"].get(identifier, {})
            data["tasks"][identifier] = {
                "solution_viewed": old.get("solution_viewed", False),
                "resets": old.get("resets", 0) + 1,
                "hints": 0,
                "passed": False,
                "updated_at": timestamp(),
            }


def is_current_pass(
    task: Task, workspace: Path, row: dict[str, Any], *, independent: bool = False
) -> bool:
    return bool(
        row.get("passed")
        and row.get("attempt_hash") == fingerprint(task, workspace)
        and (task.type != "design" or row.get("reviewed"))
        and (not independent or row.get("independent"))
    )
