# Hints

## Hint 1

The same claim folder can use different language labels while keeping its business rules unchanged. Compare the first differing field with the task's required behavior.

## Hint 2

Accumulate both audit labels across node updates. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: old.concat(update). Check every boundary input after the repair; a default-case pass alone is insufficient.
