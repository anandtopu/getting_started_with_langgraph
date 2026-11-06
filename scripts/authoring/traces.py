"""Capture local node-update evidence for Trace exercises, without hosted tracing."""

import re
from asyncio import CancelledError
from contextvars import ContextVar
from threading import Lock

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.tracers.context import register_configure_hook
from langgraph.errors import GraphInterrupt, ParentCommand

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


class NodeRecorder(BaseCallbackHandler):
    """Record callbacks directly: root run collectors need not retain child run trees."""

    def __init__(self):
        self.pending = {}
        self.updates = []
        self.lock = Lock()

    def on_chain_start(self, serialized, inputs, *, run_id, name=None, metadata=None, **kwargs):
        metadata = metadata or {}
        if name and metadata.get("langgraph_node") == name:
            with self.lock:
                self.pending[run_id] = {"node": name, "superstep": metadata.get("langgraph_step")}

    def finish(self, run_id, output, error=None):
        with self.lock:
            entry = self.pending.pop(run_id, None)
            if entry is not None:
                status = (
                    "completed"
                    if error is None
                    else "paused"
                    if isinstance(error, GraphInterrupt)
                    else "handoff"
                    if isinstance(error, ParentCommand)
                    else "cancelled"
                    if isinstance(error, CancelledError)
                    else "failed"
                )
                self.updates.append(
                    {
                        **entry,
                        "update": stable(output),
                        "status": status,
                        "failed": status == "failed",
                        "paused": status == "paused",
                        "error_type": type(error).__name__ if error is not None else None,
                    }
                )

    def on_chain_end(self, outputs, *, run_id, **kwargs):
        self.finish(run_id, outputs)

    def on_chain_error(self, error, *, run_id, **kwargs):
        output = error.args[0] if isinstance(error, ParentCommand) else None
        self.finish(run_id, output, error)


_RECORDER = ContextVar("course_node_recorder", default=None)
register_configure_hook(_RECORDER, True)


def capture(module, cases):
    evidence = []
    for case in cases:
        recorder = NodeRecorder()
        token = _RECORDER.set(recorder)
        try:
            result = observe(module, case)
        finally:
            _RECORDER.reset(token)
        evidence.append(
            {"input": case, "node_updates": recorder.updates, "observed_result": result}
        )
    return {
        "format": "Local callback node-update trace; sibling order is not a scheduling guarantee. Status distinguishes completion, approval pauses, parent-graph handoffs, cancellation, and failures. An internal control-flow exception does not imply a failed run. Empty updates mean no in-process node callback was observed: plain Python, child processes, or pre-execution rejection can produce this result.",
        "cases": evidence,
    }
