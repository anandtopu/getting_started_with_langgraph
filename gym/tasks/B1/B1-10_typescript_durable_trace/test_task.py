"""Compare the learner's written prediction with the checked execution."""

import json
from pathlib import Path


def test_written_prediction(answer):
    expected = json.loads(Path(__file__).with_name("expected_answer.json").read_text("utf-8"))
    assert answer == expected, "LARKSPUR: compare each observation and the stated cause"
