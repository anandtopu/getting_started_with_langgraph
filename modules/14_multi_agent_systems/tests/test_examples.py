"""Run each lesson against its checked boundary cases."""

import json
from pathlib import Path

import pytest

from common.exercises import observe
from common.loading import load_module

MODULE = Path(__file__).resolve().parents[1]
ROWS = []
for fixture in sorted((MODULE / "tests").glob("*.json")):
    slug = fixture.stem
    source = next((MODULE / "examples").glob("*_" + slug + ".py"))
    for row in json.loads(fixture.read_text("utf-8")):
        ROWS.append((source, row))


@pytest.mark.parametrize("source,row", ROWS)
def test_example_contract(source, row):
    from common.optional import missing_for_path

    missing = missing_for_path(source)
    if missing:
        pytest.skip(missing)
    assert observe(load_module(source), row["input"]) == row["expected"]
