"""Validated public boundaries; internal graph nodes may return partial updates."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, StrictInt


class ClaimExtraction(BaseModel):
    model_config = ConfigDict(extra="forbid")
    claim_type: Literal["water", "theft", "fire", "storm", "liability", "unknown"]
    amount_cents: StrictInt = Field(ge=0)
    loss_date: str | None = None
    confidence: float = Field(ge=0, le=1)


class Approval(BaseModel):
    model_config = ConfigDict(extra="forbid")
    decision: Literal["approve", "reject"]
    adjuster_id: str = Field(pattern=r"^ADJ-\d{3}$")
    approved_cents: StrictInt = Field(ge=0)
    reason: str = Field(min_length=1, max_length=500)
