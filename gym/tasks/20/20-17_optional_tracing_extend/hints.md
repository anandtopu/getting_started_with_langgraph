# Hints

## Hint 1

Keep the original case file and attach a corrected branch instead of erasing the disputed decision. Compare the first differing field with the task's required behavior.

## Hint 2

Keep the original route distinct from the corrected branch. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "original_route": history[0].values["route"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
