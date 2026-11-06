"""SSE data lines form one JSON payload, including CRLF and comment heartbeats."""

from common.sse import decode_events


def test_multiline_json_event_is_joined_before_parsing():
    frames = ': heartbeat\r\nid: 8\r\nevent: progress\r\ndata: {"node":\r\ndata: "review"}\r\n\r\n'
    assert decode_events(frames) == [{"id": "8", "event": "progress", "data": {"node": "review"}}]
