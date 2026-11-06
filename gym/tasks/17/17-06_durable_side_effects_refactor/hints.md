# Hints

## Hint 1

A stamped payment register prevents a duplicate even when the worker disappears before filing the receipt. Compare the first differing field with the task's required behavior.

## Hint 2

Report the durable ledger count, not an inferred execution count. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "effect_count": len(result["effects"]). Check every boundary input after the repair; a default-case pass alone is insufficient.
