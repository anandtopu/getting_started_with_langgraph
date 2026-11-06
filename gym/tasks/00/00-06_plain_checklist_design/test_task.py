"""Mechanical design checks deliberately do not score architecture quality."""


def test_design_constraints(candidate):
    choices = candidate.run()
    expected = {
        "deductible_math",
        "document_checklist",
        "classify_description",
        "open_policy_research",
        "approval_wait",
        "quote_math",
    }
    assert set(choices) == expected, "LARKSPUR: address all six design scenarios."
    assert set(choices.values()) <= {"python", "workflow", "agent"}, (
        "LARKSPUR: use a documented design choice."
    )
