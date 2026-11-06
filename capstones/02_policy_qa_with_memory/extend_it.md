# Extend it

1. Add one adversarial input and a regression test that fails before your repair.
2. Introduce a second customer or thread and prove its state and permissions remain isolated.
3. Inject a failure immediately before and after an external effect; demonstrate bounded recovery without duplication.
4. Add a retention policy with a dry-run report and scoped deletion tests.
5. Compare this design with a plain-Python baseline using correctness, latency, and operational complexity.
