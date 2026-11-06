# Hints

## Hint 1

Each desk adds a note to the same claim folder rather than throwing the folder away. Compare the first differing field with the task's required behavior.

## Hint 2

A graph node must return a mapping of state updates. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: return {"amount_cents": int(amount)}. Check every boundary input after the repair; a default-case pass alone is insufficient.
