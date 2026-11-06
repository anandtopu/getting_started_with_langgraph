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


def preserves_original(expected: Any, actual: Any) -> bool:
    """An extension may add fields/list entries, but must retain the original contract."""
    if isinstance(expected, dict):
        return isinstance(actual, dict) and all(
            key in actual and preserves_original(value, actual[key])
            for key, value in expected.items()
        )
    if isinstance(expected, list):
        return (
            isinstance(actual, list)
            and len(actual) >= len(expected)
            and all(
                preserves_original(old, new) for old, new in zip(expected, actual, strict=False)
            )
        )
    if isinstance(expected, str):
        return isinstance(actual, str) and actual == expected
    return type(actual) is type(expected) and actual == expected
