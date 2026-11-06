# Hints

## Hint 1

Try a temporarily closed service desk twice, then send the claim to review; at closing time finish the current stamped page before shelving it. Compare the first differing field with the task's required behavior.

## Hint 2

Retry the recoverable first failure before routing to manual review. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: max_attempts=2. Check every boundary input after the repair; a default-case pass alone is insufficient.
