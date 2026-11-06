"""Default tests are offline and never inherit provider credentials."""

import os

import pytest

from common.offline import install_socketpair_compatibility


def pytest_configure(config):
    install_socketpair_compatibility()


def pytest_addoption(parser):
    parser.addoption(
        "--live", action="store_true", help="Explicitly enable optional paid/provider tests."
    )
    parser.addoption(
        "--integration", action="store_true", help="Enable optional local infrastructure tests."
    )


def pytest_collection_modifyitems(config, items):
    for item in items:
        for marker, option in (("live", "--live"), ("integration", "--integration")):
            if marker in item.keywords and not config.getoption(option):
                item.add_marker(
                    pytest.mark.skip(reason=f"Optional {marker} test; enable {option} explicitly.")
                )


@pytest.fixture(autouse=True)
def offline_credentials(monkeypatch, request):
    if request.node.get_closest_marker("live") and request.config.getoption("--live"):
        request.getfixturevalue("socket_enabled")
        return
    for key in list(os.environ):
        if any(part in key.upper() for part in ("API_KEY", "ACCESS_TOKEN", "SECRET_KEY")):
            monkeypatch.delenv(key, raising=False)
    monkeypatch.setenv("LANGSMITH_TRACING", "false")
    monkeypatch.setenv("LANGCHAIN_TRACING_V2", "false")
