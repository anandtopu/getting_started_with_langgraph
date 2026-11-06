"""The only model-construction entry point for Python course code."""

import importlib.util
import json
import os
from collections.abc import Sequence
from typing import Literal
from urllib.error import URLError
from urllib.request import urlopen

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage

from common.config import PROVIDERS, ConfigurationError, Settings, load_settings
from common.fakes import ScriptedChatModel, scripted_scenario


def check_ollama(settings: Settings) -> None:
    try:
        with urlopen(settings.ollama_url + "/api/tags", timeout=settings.timeout) as response:
            models = json.load(response).get("models", [])
    except (URLError, TimeoutError, OSError, ValueError):
        raise ConfigurationError(
            "Cannot reach Ollama. Start it, then run uv run python scripts/check_env.py --live."
        ) from None
    names = {entry.get("name") for entry in models}
    if settings.model not in names and settings.model + ":latest" not in names:
        raise ConfigurationError(
            "The configured local model is not downloaded. See .env.example and scripts/check_env.py."
        )


def get_chat_model(
    *,
    mode: Literal["fake", "live"] = "fake",
    scenario: str = "acknowledge",
    responses: Sequence[AIMessage] | None = None,
    settings: Settings | None = None,
) -> BaseChatModel:
    """Create a fresh deterministic fake, or explicitly opt into a live provider."""
    if mode == "fake":
        return ScriptedChatModel(
            responses=list(responses) if responses is not None else scripted_scenario(scenario),
            temperature=0,
        )
    if mode != "live":
        raise ConfigurationError("Model mode must be fake or live.")
    if os.environ.get("LARKSPUR_OFFLINE") == "1":
        raise ConfigurationError("Live models are disabled during offline grading.")
    selected = settings or load_settings()
    key = selected.require_key()
    module_name, extra = PROVIDERS[selected.provider][2:]
    if importlib.util.find_spec(module_name) is None:
        raise ConfigurationError(
            f"Install the optional provider with uv sync --extra {extra}; "
            "then run uv run python scripts/check_env.py --live."
        )
    from langchain.chat_models import init_chat_model

    options: dict = {}
    if selected.provider == "ollama":
        check_ollama(selected)
        options.update(
            base_url=selected.ollama_url,
            temperature=0,
            num_predict=selected.max_tokens,
            client_kwargs={"timeout": selected.timeout},
        )
    else:
        options.update(api_key=key, max_tokens=selected.max_tokens, timeout=selected.timeout)
        # New reasoning models do not all accept a temperature override.
    try:
        return init_chat_model(selected.model, model_provider=selected.provider, **options)
    except (ValueError, TypeError, ImportError):
        raise ConfigurationError(
            "The live provider could not be configured. Run uv run python scripts/check_env.py --live."
        ) from None
