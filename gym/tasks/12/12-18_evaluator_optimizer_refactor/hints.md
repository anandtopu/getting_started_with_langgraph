# Hints

## Hint 1

A letter editor returns a short checklist, but has a fixed number of revision rounds. Compare the first differing field with the task's required behavior.

## Hint 2

Stop immediately once both criteria pass. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: state["accepted"] or state["attempts"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
