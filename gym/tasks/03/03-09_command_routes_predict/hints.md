# Hints

## Hint 1

One dispatch slip records both the reason and the next desk; a second independent slip can send the same case twice. Compare the first differing field with the task's required behavior.

## Hint 2

Suspicious evidence must affect the selected destination. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "review" if state["suspicious"] else "acknowledge". Check every boundary input after the repair; a default-case pass alone is insufficient.
