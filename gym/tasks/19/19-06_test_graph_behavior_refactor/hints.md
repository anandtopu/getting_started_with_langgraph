# Hints

## Hint 1

Check a ruler against known measurements instead of checking it against a second copy of the same misprinted ruler. Compare the first differing field with the task's required behavior.

## Hint 2

Require both implementations to match the independent expected route. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: row["expected"] == row["rule"] == row["graph"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
