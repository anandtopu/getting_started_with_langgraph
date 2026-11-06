"""Consistent printing with secret redaction for states, events, and checkpoints."""

import dataclasses
import json
from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel
from rich.console import Console

SECRET_WORDS = (
    "api_key",
    "password",
    "secret",
    "authorization",
    "aes_key",
    "database_url",
    "access_token",
    "refresh_token",
    "customer_token",
    "adjuster_token",
)


def safe_value(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {
            str(key): "[REDACTED]"
            if any(word in str(key).lower() for word in SECRET_WORDS)
            else safe_value(item)
            for key, item in value.items()
        }
    if isinstance(value, BaseModel):
        return safe_value(value.model_dump(mode="json"))
    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        return safe_value(dataclasses.asdict(value))
    if isinstance(value, tuple) and hasattr(value, "_asdict"):
        return safe_value(value._asdict())
    if isinstance(value, (tuple, list)):
        return [safe_value(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return f"<{type(value).__name__}>"


def print_state(value: Any, *, title: str = "State", console: Console | None = None) -> None:
    output = console or Console()
    output.print(title, style="bold")
    output.print_json(json.dumps(safe_value(value), ensure_ascii=False))


def print_stream(part: Mapping[str, Any], *, console: Console | None = None) -> None:
    print_state(part, title=f"Stream: {part.get('type', 'unknown')}", console=console)


def print_checkpoint(snapshot: Any, *, console: Console | None = None) -> None:
    print_state(snapshot, title="Checkpoint", console=console)


def print_interrupts(interrupts: Any, *, console: Console | None = None) -> None:
    print_state(interrupts, title="Interrupts", console=console)
