"""Answer-file and hint handling shared by the command line and validators."""

import json
import re
from pathlib import Path
from typing import Any


def read_hints(path: Path) -> list[str]:
    pieces = re.split(r"^## Hint [123]\s*$", path.read_text("utf-8"), flags=re.MULTILINE)[1:]
    if len(pieces) != 3 or any(not value.strip() for value in pieces):
        raise ValueError("Each task must contain exactly three nonempty numbered hints.")
    return [value.strip() for value in pieces]


def compare_answers(actual: Any, expected: Any) -> str | None:
    """JSON is structural: dictionary key order does not affect grading."""
    if actual == expected:
        return None
    return (
        "The prediction differs from the deterministic run.\n"
        + "Your answer: "
        + json.dumps(actual, sort_keys=True)
        + "\nExpected: "
        + json.dumps(expected, sort_keys=True)
    )
