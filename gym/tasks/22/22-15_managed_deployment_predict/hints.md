# Hints

## Hint 1

A service definition, a case folder, and a work session are three different identifiers. Compare the first differing field with the task's required behavior.

## Hint 2

Require both assistant configuration and thread identity. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: if not case["assistant_id"] or not case["thread_id"]:. Check every boundary input after the repair; a default-case pass alone is insufficient.
