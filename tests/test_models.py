"""Configuration and provider boundaries, without live model calls."""

from dataclasses import replace
from unittest.mock import patch

import pytest

from common.config import ROOT, ConfigurationError, load_settings
from common.models import get_chat_model


def test_documented_provider_switch_and_override():
    local = load_settings(environ={})
    hosted = load_settings(environ={"LLM_PROVIDER": "openai"})
    assert local.provider == "ollama"
    assert hosted.provider == "openai"
    assert hosted.model != local.model
    assert load_settings(environ={"LLM_PROVIDER": "google"}).provider == "google_genai"
    assert (
        load_settings(environ={"LLM_MODEL": "deliberate-test-override"}).model
        == "deliberate-test-override"
    )


def test_precedence_and_secret_redaction(tmp_path):
    (tmp_path / ".env.example").write_text(
        (ROOT / ".env.example").read_text("utf-8"), encoding="utf-8"
    )
    (tmp_path / ".env").write_text(
        "LLM_PROVIDER=openai\nOPENAI_API_KEY=private-value\nLLM_MODEL=file-model\n",
        encoding="utf-8",
    )
    settings = load_settings(tmp_path, {"LLM_MODEL": "process-model"})
    assert settings.model == "process-model"
    assert settings.require_key() == "private-value"
    assert "private-value" not in repr(settings)


@pytest.mark.parametrize(
    "values",
    [
        {"LLM_PROVIDER": "not-a-provider"},
        {"LLM_MAX_TOKENS": "-1"},
        {"LLM_MAX_TOKENS": "bad"},
        {"LLM_TIMEOUT_SECONDS": "0"},
    ],
)
def test_invalid_settings_are_friendly(values):
    with pytest.raises(ConfigurationError):
        load_settings(environ=values)


def test_fake_never_needs_settings_or_provider_imports():
    with patch("common.models.load_settings", side_effect=AssertionError("must stay offline")):
        assert get_chat_model().invoke("claim").content


def test_missing_key_is_not_a_stack_of_provider_details():
    settings = load_settings(environ={"LLM_PROVIDER": "openai"})
    with pytest.raises(ConfigurationError, match="check_env.py"):
        get_chat_model(mode="live", settings=settings)


def test_live_construction_uses_one_init_helper():
    settings = load_settings(
        environ={"LLM_PROVIDER": "anthropic", "ANTHROPIC_API_KEY": "synthetic-test-key"}
    )
    with (
        patch("common.models.importlib.util.find_spec", return_value=True),
        patch("langchain.chat_models.init_chat_model") as initialize,
    ):
        get_chat_model(mode="live", settings=settings)
    assert initialize.call_args.kwargs["model_provider"] == "anthropic"
    assert "temperature" not in initialize.call_args.kwargs


def test_ollama_service_failure_has_friendly_message():
    settings = load_settings(environ={})
    with (
        patch("common.models.importlib.util.find_spec", return_value=True),
        patch("common.models.urlopen", side_effect=OSError),
        pytest.raises(ConfigurationError, match="Start it"),
    ):
        get_chat_model(mode="live", settings=settings)


def test_missing_optional_adapter_explains_extra():
    settings = replace(
        load_settings(environ={}), provider="openai", secrets={"OPENAI_API_KEY": "synthetic"}
    )
    with (
        patch("common.models.importlib.util.find_spec", return_value=None),
        pytest.raises(ConfigurationError, match="--extra openai"),
    ):
        get_chat_model(mode="live", settings=settings)
