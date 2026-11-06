# Hints

## Hint 1

A policy lookup card belongs to a customer and policy version, not just the shelf where it was found. Compare the first differing field with the task's required behavior.

## Hint 2

The cache must observe the injected clock advancing. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: ClockCache(lambda: clock[0]). Check every boundary input after the repair; a default-case pass alone is insufficient.
