"""Fixtures and machine-readable results used only by the gym's grading subprocess."""

import json
import sys
from pathlib import Path
from typing import Any

import pytest

from common.loading import load_module
from common.offline import block_network, install_socketpair_compatibility

_RESULTS: list[dict[str, Any]] = []


def pytest_addoption(parser: Any) -> None:
    parser.addoption("--candidate", required=True, help="The learner attempt to grade.")
    parser.addoption("--gym-report", required=True, help="Machine-readable result destination.")


def pytest_configure(config: Any) -> None:
    _RESULTS.clear()
    install_socketpair_compatibility()
    sys.addaudithook(block_network)


@pytest.fixture
def candidate_path(pytestconfig: Any) -> Path:
    return Path(pytestconfig.getoption("--candidate")).resolve()


@pytest.fixture
def candidate(candidate_path: Path) -> Any:
    return load_module(candidate_path)


@pytest.fixture
def answer(candidate_path: Path) -> Any:
    return json.loads(candidate_path.read_text("utf-8"))


def pytest_runtest_logreport(report: Any) -> None:
    if report.when == "call" or report.failed:
        _RESULTS.append(
            {
                "nodeid": report.nodeid,
                "when": report.when,
                "outcome": report.outcome,
                "detail": report.longreprtext if report.failed else "",
            }
        )


def pytest_sessionfinish(session: Any, exitstatus: int) -> None:
    Path(session.config.getoption("--gym-report")).write_text(
        json.dumps({"exit_code": int(exitstatus), "tests": _RESULTS}, indent=2),
        encoding="utf-8",
    )
