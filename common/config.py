"""Load documented settings without printing secrets or mutating the process environment."""

import os
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import dotenv_values

ROOT = Path(__file__).resolve().parents[1]
PROVIDERS = {
    "ollama": ("OLLAMA_MODEL", "", "langchain_ollama", "ollama"),
    "openai": ("OPENAI_MODEL", "OPENAI_API_KEY", "langchain_openai", "openai"),
    "anthropic": ("ANTHROPIC_MODEL", "ANTHROPIC_API_KEY", "langchain_anthropic", "anthropic"),
    "google_genai": ("GOOGLE_MODEL", "GOOGLE_API_KEY", "langchain_google_genai", "google"),
}


class ConfigurationError(ValueError):
    """A configuration problem whose message is safe to display."""


@dataclass(frozen=True)
class Settings:
    provider: str
    model: str
    ollama_url: str
    max_tokens: int
    timeout: float
    secrets: dict[str, str] = field(default_factory=dict, repr=False)
    tracing: bool = False

    def require_key(self) -> str | None:
        key_name = PROVIDERS[self.provider][1]
        if key_name and not self.secrets.get(key_name):
            raise ConfigurationError(
                f"Set {key_name} in .env for optional live runs. "
                "Run: uv run python scripts/check_env.py --live"
            )
        return self.secrets.get(key_name)


def load_settings(root: Path = ROOT, environ: Mapping[str, str] | None = None) -> Settings:
    """Precedence is process environment, local .env, then the documented template."""
    values = dict(dotenv_values(root / ".env.example"))
    values.update(dotenv_values(root / ".env"))
    values.update(os.environ if environ is None else environ)
    provider = str(values.get("LLM_PROVIDER") or "ollama").strip().lower()
    provider = {"google": "google_genai", "gemini": "google_genai"}.get(provider, provider)
    if provider not in PROVIDERS:
        raise ConfigurationError("LLM_PROVIDER must be ollama, openai, anthropic, or google_genai.")
    model = str(values.get("LLM_MODEL") or values.get(PROVIDERS[provider][0]) or "").strip()
    if not model:
        raise ConfigurationError(
            "Choose a model in .env; see .env.example and scripts/check_env.py."
        )
    try:
        max_tokens = int(str(values.get("LLM_MAX_TOKENS") or "512"))
        timeout = float(str(values.get("LLM_TIMEOUT_SECONDS") or "10"))
    except ValueError:
        raise ConfigurationError("Token and timeout settings must be numeric.") from None
    if not 1 <= max_tokens <= 32768 or not 0 < timeout <= 120:
        raise ConfigurationError("Use 1–32768 response tokens and a timeout of 1–120 seconds.")
    keys = ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY", "LANGSMITH_API_KEY")
    return Settings(
        provider=provider,
        model=model,
        ollama_url=str(values.get("OLLAMA_BASE_URL") or "http://localhost:11434").rstrip("/"),
        max_tokens=max_tokens,
        timeout=timeout,
        secrets={key: str(values.get(key) or "") for key in keys},
        tracing=str(values.get("LANGSMITH_TRACING") or "false").lower() == "true",
    )
