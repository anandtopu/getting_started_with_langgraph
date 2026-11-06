# Hints

## Hint 1

Each numbered work order carries its own approval form with only the choices that desk is allowed to accept. Compare the first differing field with the task's required behavior.

## Hint 2

Respect rejection instead of coercing every decision to approval. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: decision = {"type": case["decision"]}. Check every boundary input after the repair; a default-case pass alone is insufficient.
