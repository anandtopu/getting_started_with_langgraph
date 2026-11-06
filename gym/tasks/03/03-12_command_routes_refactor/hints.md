# Hints

## Hint 1

One dispatch slip records both the reason and the next desk; a second independent slip can send the same case twice. Compare the first differing field with the task's required behavior.

## Hint 2

Equivalent control flow must not duplicate work. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "visited": ["review"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
