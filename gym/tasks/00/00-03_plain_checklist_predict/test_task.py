"""Compare the learner prediction with the actual checklist run."""

from common.claims import checklist
from common.gym_fixtures import checklist_cases
from gym.answers import compare_answers


def test_prediction(answer):
    outcomes = [checklist(claim) for claim in checklist_cases()]
    expected = {
        "statuses": [item["status"] for item in outcomes],
        "missing": [item["missing"] for item in outcomes],
        "trace": outcomes[0]["trace"],
    }
    difference = compare_answers(answer, expected)
    assert difference is None, "LARKSPUR: " + str(difference)
