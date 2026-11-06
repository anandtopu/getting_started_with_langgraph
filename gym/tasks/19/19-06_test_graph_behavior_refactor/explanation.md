# Why the refactor works

A pytest test is a function whose assertions express requirements. Parametrized tests run it over many inputs. Compare pure node rules and whole graphs against independently specified boundary outcomes; comparing two copies of the same implementation can preserve the same bug. Fake models make orchestration tests repeatable, not model accuracy measurable.

Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.

The starter is a working behavioral baseline. The reference changes its design, then runs the same case fixtures and a separate structural check. Inspect both test groups: matching one happy-path output does not prove equivalence. Preserve rejection/error behavior and input ownership as well as successful results.

Run the selected workspace file through gym check. Viewing the reference is recorded as assisted study.
