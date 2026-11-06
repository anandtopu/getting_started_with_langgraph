"""Exercise every public command and protect learner files."""

import shutil

import pytest

from gym.catalog import Catalog
from gym.cli import copy_attempt, main
from gym.progress import ProgressStore, fingerprint


def run_cli(workspace, *arguments):
    return main(["--workspace", str(workspace), *arguments])


def test_list_filters_and_planned_task_error(tmp_path, capsys):
    assert run_cli(tmp_path, "list", "--module", "03", "--type", "fix", "--level", "medium") == 0
    output = capsys.readouterr().out
    assert "03-02" in output and "00-01" not in output
    planned = next((task for task in Catalog().tasks.values() if not task.available), None)
    if planned is not None:
        assert run_cli(tmp_path, "start", planned.id) == 2
        assert "later phase" in capsys.readouterr().err
    assert run_cli(tmp_path, "start", "../.env") == 2


def test_start_hint_solution_and_reset(tmp_path, capsys, monkeypatch):
    assert run_cli(tmp_path, "start", "00-01") == 0
    attempt = tmp_path / "00-01.py"
    attempt.write_text("# My preserved attempt\n", encoding="utf-8")
    assert run_cli(tmp_path, "start", "00-01") == 2
    assert attempt.read_text("utf-8") == "# My preserved attempt\n"
    for _ in range(4):
        assert run_cli(tmp_path, "hint", "00-01") == 0
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert run_cli(tmp_path, "solution", "00-01") == 0
    assert not ProgressStore(tmp_path).read()["tasks"]["00-01"].get("solution_viewed")
    assert run_cli(tmp_path, "solution", "00-01", "--yes") == 0
    assert ProgressStore(tmp_path).read()["tasks"]["00-01"]["solution_viewed"]
    assert run_cli(tmp_path, "reset", "00-01") == 0
    assert attempt.read_text("utf-8") == "# My preserved attempt\n"
    assert run_cli(tmp_path, "reset", "00-01", "--yes") == 0
    backup = next(tmp_path.glob(".backups/*/00-01.py"))
    assert backup.read_text("utf-8") == "# My preserved attempt\n"
    assert "# YOUR CODE HERE" in attempt.read_text("utf-8")


def test_code_check_loads_the_selected_attempt(tmp_path, capsys):
    catalog = Catalog()
    task = catalog.get("00-01")
    assert run_cli(tmp_path, "start", task.id) == 0
    assert run_cli(tmp_path, "check", task.id) == 1
    assert "NOT YET" in capsys.readouterr().out
    shutil.copyfile(task.folder / "solution.py", task.attempt_path(tmp_path))
    assert run_cli(tmp_path, "check", task.id) == 0
    assert ProgressStore(tmp_path).read()["tasks"][task.id]["passed"]
    # A plausible but wrong learner function must fail even though the reference still exists.
    task.attempt_path(tmp_path).write_text("def run(claim):\n    return {}\n", encoding="utf-8")
    assert run_cli(tmp_path, "check", task.id) == 1


@pytest.mark.parametrize("identifier", ["00-03", "00-04"])
def test_answer_files_are_graded(tmp_path, identifier):
    task = Catalog().get(identifier)
    assert run_cli(tmp_path, "start", identifier) == 0
    assert run_cli(tmp_path, "check", identifier) == 1
    shutil.copyfile(task.folder / "expected_answer.json", task.attempt_path(tmp_path))
    assert run_cli(tmp_path, "check", identifier) == 0


def test_progress_next_and_empty_drill(tmp_path, capsys):
    assert run_cli(tmp_path, "progress") == 0
    assert run_cli(tmp_path, "next") == 0
    assert "Next: 00-01" in capsys.readouterr().out
    assert run_cli(tmp_path, "drill", "--seed", "7") == 0
    assert "Finish one module" in capsys.readouterr().out


def test_progress_distinguishes_help_from_full_mastery(tmp_path, capsys):
    task = Catalog().get("00-01")
    copy_attempt(task, tmp_path)
    store = ProgressStore(tmp_path)
    store.update(task.id, hints=1, solution_viewed=True)
    store.record_check(task, fingerprint(task, tmp_path), True)
    assert run_cli(tmp_path, "progress") == 0
    output = capsys.readouterr().out
    assert "Started: 1; hints used: 1; solutions viewed: 1; full mastery: pending" in output
    assert run_cli(tmp_path, "list", "--available") == 0
    assert "guided milestone: yes" in capsys.readouterr().out


def test_seeded_drill_preserves_main_attempts(tmp_path):
    catalog = Catalog()
    store = ProgressStore(tmp_path)
    for task in catalog.available():
        copy_attempt(task, tmp_path)
        source = task.folder / ("expected_answer.json" if task.answer_task else "solution.py")
        shutil.copyfile(source, task.attempt_path(tmp_path))
        store.record_check(task, fingerprint(task, tmp_path), True, reviewed=True)
    original = {path.name: path.read_bytes() for path in tmp_path.glob("00-*")}
    assert run_cli(tmp_path, "drill", "--seed", "7") == 0
    first = store.read()["drills"][-1]
    assert run_cli(tmp_path, "drill", "--seed", "7") == 0
    second = store.read()["drills"][-1]
    assert first["task_id"] == second["task_id"] and first["attempt"] != second["attempt"]
    assert original == {path.name: path.read_bytes() for path in tmp_path.glob("00-*")}
    assert run_cli(tmp_path, "check", first["task_id"], "--attempt", first["attempt"]) == 1
    assert store.read()["drills"][0]["passed"] is False
