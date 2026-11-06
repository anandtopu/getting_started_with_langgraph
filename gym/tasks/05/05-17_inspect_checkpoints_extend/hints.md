# Hints

## Hint 1

Correct an audit ledger by adding a new entry with a parent reference instead of erasing an old entry. Compare the first differing field with the task's required behavior.

## Hint 2

Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: the new node or boundary contract described above. Check every boundary input after the repair; a default-case pass alone is insufficient.
