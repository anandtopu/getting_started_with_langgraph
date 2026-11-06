# Hints

## Hint 1

The same claim folder can use different language labels while keeping its business rules unchanged. Compare the first differing field with the task's required behavior.

## Hint 2

Handle an empty normalized description as missing information. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: !state.description ?. Check every boundary input after the repair; a default-case pass alone is insufficient.
