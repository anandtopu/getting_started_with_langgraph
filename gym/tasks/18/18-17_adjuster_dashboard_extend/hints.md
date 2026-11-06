# Hints

## Hint 1

Replace an outdated approval form when the desk sends a corrected one instead of keeping both forms active. Compare the first differing field with the task's required behavior.

## Hint 2

Enable submission only for a currently pending interrupt. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: case["submitted_id"] in {item["id"] for item in state["pending"]}. Check every boundary input after the repair; a default-case pass alone is insufficient.
