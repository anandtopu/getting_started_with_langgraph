"""Synthetic graph export for the local Agent Server and optional Studio."""

from langgraph.graph import END

from common.copilot.v02 import build_builder
from common.copilot.v03 import approve_claim

builder = build_builder()
builder.add_node("approve_claim", approve_claim)
builder.add_edge("route", "approve_claim")
builder.add_edge("approve_claim", END)
# The Agent Server owns persistence. Do not install a second saver in this export.
graph = builder.compile()
