# Hints

## Hint 1

Correct an audit ledger by adding a new entry with a parent reference instead of erasing an old entry. Compare the first differing field with the task's required behavior.

## Hint 2

Continue the configuration returned by update_state, not an unrelated checkpoint. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: graph.invoke(None, corrected, version="v2"). Check every boundary input after the repair; a default-case pass alone is insufficient.
