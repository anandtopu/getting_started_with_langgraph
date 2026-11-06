# Hints

## Hint 1

The same claim folder can use different language labels while keeping its business rules unchanged. Compare the first differing field with the task's required behavior.

## Hint 2

Extract reusable graph construction into buildGraph; keep invocation, saver lifetime, stream counts, and all old behavior unchanged. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: the original behavioral contract. Check every boundary input after the repair; a default-case pass alone is insufficient.
