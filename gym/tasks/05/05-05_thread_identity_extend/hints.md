# Hints

## Hint 1

The thread ID is the claim-folder number; reuse another customer's number and you open the wrong folder. Compare the first differing field with the task's required behavior.

## Hint 2

Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: the new node or boundary contract described above. Check every boundary input after the repair; a default-case pass alone is insufficient.
