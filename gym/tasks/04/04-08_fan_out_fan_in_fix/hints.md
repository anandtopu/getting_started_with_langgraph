# Hints

## Hint 1

An adjuster collects reports from several specialists and signs only after the slowest specialist finishes. Compare the first differing field with the task's required behavior.

## Hint 2

Parallel writes to an overwrite channel conflict. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: findings: Annotated[list[str], operator.add]. Check every boundary input after the repair; a default-case pass alone is insufficient.
