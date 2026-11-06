"""A grader cannot pass skipped checks, an unrelated solution, or a hanging process."""

import sys
from dataclasses import replace

from common.data import ROOT
from common.process import offline_environment, run_process
from gym.catalog import Catalog
from gym.runner import check_task


def test_timeout_is_reported_without_hanging(tmp_path):
    task = replace(Catalog().get("00-01"), timeout=2)
    attempt = tmp_path / "attempt.py"
    attempt.write_text("def run(claim):\n    while True:\n        continue\n", encoding="utf-8")
    result = check_task(task, attempt)
    assert not result.passed and result.timed_out and result.returncode == 124


def test_skipped_task_tests_are_not_a_pass(tmp_path):
    task = Catalog().get("00-01")
    (tmp_path / "test_task.py").write_text(
        "import pytest\n\n@pytest.mark.skip(reason='bad grader')\ndef test_nothing():\n    assert False\n",
        encoding="utf-8",
    )
    candidate = tmp_path / "candidate.py"
    candidate.write_text("value = 1\n", encoding="utf-8")
    result = check_task(replace(task, folder=tmp_path), candidate)
    assert not result.passed and "skipped tests" in result.output


def test_environment_removes_credentials(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "must-not-reach-child")
    monkeypatch.setenv("PRIVATE_ACCESS_TOKEN", "must-not-reach-child")
    environment = offline_environment()
    assert "OPENAI_API_KEY" not in environment and "PRIVATE_ACCESS_TOKEN" not in environment
    assert environment["LANGSMITH_TRACING"] == "false"


def test_one_pass_does_not_hide_a_skipped_acceptance_check(tmp_path):
    task = replace(Catalog().get("00-01"), folder=tmp_path)
    (tmp_path / "test_task.py").write_text(
        "import pytest\ndef test_good():\n    assert True\n"
        "@pytest.mark.skip(reason='missing acceptance')\ndef test_missing():\n    assert False\n",
        encoding="utf-8",
    )
    candidate = tmp_path / "candidate.py"
    candidate.write_text("value = 1\n", encoding="utf-8")
    result = check_task(task, candidate)
    assert not result.passed and result.returncode == 5
    assert any(item["outcome"] == "skipped" for item in result.tests)


def test_child_network_is_blocked(tmp_path):
    attempt = tmp_path / "network.py"
    attempt.write_text(
        "import socket\nsocket.create_connection(('example.com', 443), timeout=1)\n",
        encoding="utf-8",
    )
    result = run_process(
        [sys.executable, "-m", "common.offline", str(attempt)], cwd=ROOT, env=offline_environment()
    )
    assert result.returncode != 0
    assert "Offline course execution attempted network access" in result.stdout


def test_grader_blocks_dns_before_loading_learner_code(tmp_path):
    task = Catalog().get("00-01")
    attempt = tmp_path / "dns.py"
    attempt.write_text(
        "import socket\nsocket.getaddrinfo('example.com', 443)\n",
        encoding="utf-8",
    )
    result = check_task(task, attempt)
    assert not result.passed
    assert (
        "SocketBlockedError" in result.output
        or "Offline course execution attempted network access" in result.output
    )
