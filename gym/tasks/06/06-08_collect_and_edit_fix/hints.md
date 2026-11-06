# Hints

## Hint 1

Return two forms using their tracking numbers instead of assuming they arrived in desk order. Compare the first differing field with the task's required behavior.

## Hint 2

Each interrupt must receive the response for its own request kind. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: case[item.value["kind"]]. Check every boundary input after the repair; a default-case pass alone is insufficient.
