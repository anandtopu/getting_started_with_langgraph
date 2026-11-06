"""Capture local node-update evidence for Trace exercises, without hosted tracing."""

import re

from langchain_core.tracers.context import collect_runs

from common.exercises import observe
from common.pretty import safe_value


def stable(value):
    value = safe_value(value)
    if isinstance(value, dict):
        return {
            key: stable(item)
            for key, item in value.items()
            if key not in {"checkpoint_ns", "checkpoint_id"}
        }
    if isinstance(value, list):
        return [stable(item) for item in value]
    if isinstance(value, str):
        return re.sub(
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", "<runtime-id>", value
        )
    return value


def capture(module, cases):
    evidence = []
    for case in cases:
        with collect_runs() as collector:
            result = observe(module, case)
        updates = []

        def visit(run, updates=updates):
            metadata = run.extra.get("metadata", {})
            if metadata.get("langgraph_node") == run.name:
                updates.append(
                    {
                        "node": run.name,
                        "superstep": metadata.get("langgraph_step"),
                        "update": stable(run.outputs),
                        "failed": bool(run.error),
                    }
                )
            for child in run.child_runs:
                visit(child)

        for run in collector.traced_runs:
            visit(run)
        evidence.append({"input": case, "node_updates": updates, "observed_result": result})
    return {
        "format": "Local callback node-update trace; sibling order is not a scheduling guarantee. Empty updates mean execution is outside this process or uses plain Python.",
        "cases": evidence,
    }
