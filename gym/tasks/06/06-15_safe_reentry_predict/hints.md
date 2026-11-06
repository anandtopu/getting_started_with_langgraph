# Hints

## Hint 1

A clerk rereads the form after approval; rereading must not send a second payment notice. Compare the first differing field with the task's required behavior.

## Hint 2

Rejection must not trigger the synthetic notification. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: if state["approved"]:. Check every boundary input after the repair; a default-case pass alone is insufficient.
