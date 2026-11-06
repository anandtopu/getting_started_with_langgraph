# Hints

## Hint 1

Correct an audit ledger by adding a new entry with a parent reference instead of erasing an old entry. Compare the first differing field with the task's required behavior.

## Hint 2

The edit attribution determines the pending successor nodes. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: as_node="normalize". Check every boundary input after the repair; a default-case pass alone is insufficient.
