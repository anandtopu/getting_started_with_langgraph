# Hints

## Hint 1

Retain a ledger of additions with occasional full copies, then rebuild the current folder from those records. Compare the first differing field with the task's required behavior.

## Hint 2

Retain earlier delta writes when applying a new batch. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: result.extend(write). Check every boundary input after the repair; a default-case pass alone is insufficient.
