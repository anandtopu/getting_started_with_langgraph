# Hints

## Hint 1

If a receipt is lost, resend the same numbered order rather than creating a second order. Compare the first differing field with the task's required behavior.

## Hint 2

Raise only when the transient retry budget is exhausted. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: if attempt + 1 == attempts:. Check every boundary input after the repair; a default-case pass alone is insufficient.
