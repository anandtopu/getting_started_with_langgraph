# Hints

## Hint 1

Two service-desk layouts must produce the same numbered work orders and final explanation. Compare the first differing field with the task's required behavior.

## Hint 2

Replace the manual model/tool loop with createAgent, keeping message roles, call IDs, errors, and final text unchanged. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: the original behavioral contract. Check every boundary input after the repair; a default-case pass alone is insufficient.
