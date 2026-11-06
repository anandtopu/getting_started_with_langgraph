# Why the refactor works

A manual agent loop alternates a model node and ToolNode. tools_condition checks the newest AI message: tool calls continue the loop, a final answer ends it. A recursion budget catches nontermination, but does not authorize tool effects or guarantee a useful answer.

Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.

The starter is a working behavioral baseline. The reference changes its design, then runs the same case fixtures and a separate structural check. Inspect both test groups: matching one happy-path output does not prove equivalence. Preserve rejection/error behavior and input ownership as well as successful results.

Run the selected workspace file through gym check. Viewing the reference is recorded as assisted study.
