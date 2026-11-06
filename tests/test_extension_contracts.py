"""Compatibility checks permit new fields but reject changed values, order, and booleans."""

from common.exercises import preserves_original


def test_preservation_rejects_behavior_changes_but_accepts_json_string_subclasses():
    class Text(str):
        pass

    assert preserves_original(
        {"text": "hello", "steps": ["a"]}, {"text": Text("hello"), "steps": ["a", "b"], "new": True}
    )
    assert not preserves_original({"approved": False}, {"approved": True})
    assert not preserves_original({"amount": 1}, {"amount": True})
    assert not preserves_original({"steps": ["a", "b"]}, {"steps": ["b", "a"]})
