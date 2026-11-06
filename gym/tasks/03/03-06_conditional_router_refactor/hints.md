# Hints

## Hint 1

A sorting desk labels envelopes; the delivery map tells the courier which desk each label means. Compare the first differing field with the task's required behavior.

## Hint 2

Refactoring must retain the missing-evidence route. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: if state["missing"]:. Check every boundary input after the repair; a default-case pass alone is insufficient.
