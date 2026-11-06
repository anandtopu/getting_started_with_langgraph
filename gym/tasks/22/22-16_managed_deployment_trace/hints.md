# Hints

## Hint 1

A service definition, a case folder, and a work session are three different identifiers. Compare the first differing field with the task's required behavior.

## Hint 2

Keep interactive waiting distinct from background execution. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "background" if case["background"] else "wait". Check every boundary input after the repair; a default-case pass alone is insufficient.
