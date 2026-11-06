"""Small grading utilities; expected answers live in exercise fixtures, never here."""

from copy import deepcopy
from typing import Any

from common.pretty import safe_value


def observe(module: Any, case: dict) -> dict:
    """Keep intentional runtime failures inspectable without hiding import failures."""
    try:
        return {"value": safe_value(module.run(deepcopy(case)))}
    except Exception as error:
        return {"error": type(error).__name__}


def read_path(value: Any, path: str) -> Any:
    for component in path.split("."):
        value = value[int(component)] if isinstance(value, list) else value[component]
    return value
