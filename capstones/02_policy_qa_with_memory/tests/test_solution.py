"""Independent acceptance checks; select an attempt with LARKSPUR_CAPSTONE_FILE."""

import json
import os
from pathlib import Path

import pytest

from common.loading import load_module

FOLDER = Path(__file__).resolve().parents[1]
CASES = [json.loads(line) for line in (FOLDER / "eval/cases.jsonl").read_text("utf-8").splitlines()]


@pytest.mark.parametrize("case", CASES)
def test_acceptance(case):
    candidate = load_module(Path(os.environ.get("LARKSPUR_CAPSTONE_FILE", FOLDER / "solution.py")))
    expected = case["expected"]
    if "error" in expected:
        with pytest.raises(Exception) as error:
            candidate.run(case["input"])
        assert type(error.value).__name__ == expected["error"]
    else:
        actual = candidate.run(case["input"])
        for key, value in expected.items():
            assert actual[key] == value, "CAPSTONE: " + key
