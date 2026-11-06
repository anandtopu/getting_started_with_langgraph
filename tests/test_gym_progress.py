"""Progress survives interruption, concurrent writers, and changed attempts."""

import json
import multiprocessing
import shutil
from dataclasses import replace

import pytest

from gym.catalog import Catalog
from gym.cli import copy_attempt
from gym.progress import ProgressStore, fingerprint, is_current_pass


def write_progress(directory, identifier):
    ProgressStore(directory).update(identifier, started=True)


@pytest.mark.parametrize(
    "payload",
    [
        {"schema_version": 1, "tasks": {"00-01": {"hints": "bad"}}, "drills": []},
        {"schema_version": 1, "tasks": {}, "drills": ["bad"]},
    ],
)
def test_nested_corruption_is_preserved_and_recovered(tmp_path, payload):
    store = ProgressStore(tmp_path)
    original = json.dumps(payload)
    store.path.write_text(original, encoding="utf-8")
    assert store.read() == {"schema_version": 1, "tasks": {}, "drills": []}
    backups = list(tmp_path.glob(".progress.corrupt-*.json"))
    assert len(backups) == 1 and backups[0].read_text("utf-8") == original


def test_atomic_progress_and_stale_pass(tmp_path):
    task = Catalog().get("00-01")
    copy_attempt(task, tmp_path)
    store = ProgressStore(tmp_path)
    digest = fingerprint(task, tmp_path)
    store.record_check(task, digest, True)
    assert is_current_pass(task, tmp_path, store.read()["tasks"][task.id], independent=True)
    with task.attempt_path(tmp_path).open("a", encoding="utf-8") as output:
        output.write("\n# learner edit\n")
    assert not is_current_pass(task, tmp_path, store.read()["tasks"][task.id])


def test_changed_acceptance_contract_invalidates_an_old_pass(tmp_path):
    original = Catalog().get("00-01")
    folder = tmp_path / "task"
    shutil.copytree(original.folder, folder)
    task = replace(original, folder=folder)
    workspace = tmp_path / "work"
    copy_attempt(task, workspace)
    store = ProgressStore(workspace)
    store.record_check(task, fingerprint(task, workspace), True)
    row = store.read()["tasks"][task.id]
    assert is_current_pass(task, workspace, row)
    with (folder / "test_task.py").open("a", encoding="utf-8") as output:
        output.write("\ndef test_new_requirement():\n    assert False\n")
    assert not is_current_pass(task, workspace, row)


def test_solution_exposure_persists_after_reset(tmp_path):
    task = Catalog().get("00-01")
    copy_attempt(task, tmp_path)
    store = ProgressStore(tmp_path)
    store.update(task.id, solution_viewed=True)
    store.record_check(task, fingerprint(task, tmp_path), True)
    assert not store.read()["tasks"][task.id]["independent"]
    store.reset(task.id)
    assert store.read()["tasks"][task.id]["solution_viewed"]


def test_corrupt_progress_is_preserved(tmp_path):
    (tmp_path / ".progress.json").write_text("{broken", encoding="utf-8")
    store = ProgressStore(tmp_path)
    assert store.read()["tasks"] == {}
    backups = list(tmp_path.glob(".progress.corrupt-*.json"))
    assert len(backups) == 1 and backups[0].read_text("utf-8") == "{broken"
    assert store.recovery_message


def test_newer_progress_version_is_not_overwritten(tmp_path):
    path = tmp_path / ".progress.json"
    original = json.dumps({"schema_version": 999, "tasks": {}, "drills": []})
    path.write_text(original, encoding="utf-8")
    with pytest.raises(RuntimeError, match="unsupported"):
        ProgressStore(tmp_path).read()
    assert path.read_text("utf-8") == original


def test_hint_count_is_bounded(tmp_path):
    store = ProgressStore(tmp_path)
    assert [store.next_hint("00-01") for _ in range(5)] == [0, 1, 2, 3, 3]
    assert store.read()["tasks"]["00-01"]["hints"] == 3


def test_concurrent_processes_do_not_lose_updates(tmp_path):
    context = multiprocessing.get_context("spawn")
    workers = [
        context.Process(target=write_progress, args=(tmp_path, f"task-{i}")) for i in range(4)
    ]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join(15)
        assert worker.exitcode == 0
    assert len(ProgressStore(tmp_path).read()["tasks"]) == 4


def test_design_needs_explicit_review(tmp_path):
    task = Catalog().get("00-06")
    copy_attempt(task, tmp_path)
    shutil.copyfile(task.folder / "solution.py", task.attempt_path(tmp_path))
    store = ProgressStore(tmp_path)
    digest = fingerprint(task, tmp_path)
    store.record_check(task, digest, True)
    assert not is_current_pass(task, tmp_path, store.read()["tasks"][task.id])
    store.record_check(task, digest, True, reviewed=True)
    assert is_current_pass(task, tmp_path, store.read()["tasks"][task.id])
