"""Public SSE frames and dashboard projections; internal checkpoint contents stay private."""

import json

from common.pretty import safe_value


def encode_event(event: str, data: dict, sequence: int) -> str:
    if not event.replace("_", "").isalnum() or sequence < 0:
        raise ValueError("Invalid SSE event identity")
    return f"id: {sequence}\nevent: {event}\ndata: {json.dumps(safe_value(data), separators=(',', ':'))}\n\n"


def decode_events(text: str) -> list[dict]:
    events = []
    for frame in text.replace("\r\n", "\n").split("\n\n"):
        fields = {}
        data_lines = []
        for line in frame.splitlines():
            if line and not line.startswith(":") and ":" in line:
                key, value = line.split(":", 1)
                value = value.removeprefix(" ")
                if key == "data":
                    data_lines.append(value)
                else:
                    fields[key] = value
        if data_lines:
            events.append(
                {
                    "id": fields.get("id"),
                    "event": fields.get("event", "message"),
                    "data": json.loads("\n".join(data_lines)),
                }
            )
    return events


def update_dashboard(state: dict, event: dict) -> dict:
    result = {**state, "progress": list(state.get("progress", []))}
    kind, data = event["event"], event["data"]
    if kind == "progress":
        result["progress"].append(data["node"])
    elif kind == "token":
        result["text"] = result.get("text", "") + data["text"]
    elif kind == "snapshot":
        result["snapshot"] = data
        result["pending"] = data["interrupts"]
    elif kind == "error":
        result["error"] = data["message"]
    return result
