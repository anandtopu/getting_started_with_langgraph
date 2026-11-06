# Hints

## Hint 1

Two inspectors can report in either order, but the adjuster signs after both reports arrive. Compare the first differing field with the task's required behavior.

## Hint 2

Nested updates require subgraph streaming. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: subgraphs=True. Check every boundary input after the repair; a default-case pass alone is insufficient.
