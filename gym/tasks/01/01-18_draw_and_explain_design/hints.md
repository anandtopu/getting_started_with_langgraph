# Hints

## Hint 1

Compare the building plan with the visitor log: one describes possibilities, the other records a visit. Compare the first differing field with the task's required behavior.

## Hint 2

The diagram must include validation on the executed route. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: graph.add_edge("receive", "validate"). Check every boundary input after the repair; a default-case pass alone is insufficient.
