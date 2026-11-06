# Hints

## Hint 1

A rejected form still receives a reason stamp before leaving the queue. Compare the first differing field with the task's required behavior.

## Hint 2

Zero is a defined boundary, not an omitted case. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: amount < 0. Check every boundary input after the repair; a default-case pass alone is insufficient.
