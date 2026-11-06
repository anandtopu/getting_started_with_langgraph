"""Exercise real HTTP authorization, stale decisions, leases, and durable effect keys."""

import pytest

pytest.importorskip("fastapi", reason="Install the apps extra for API tests")

from common.app_demo import exercise_api
from common.effects import EffectLedger
from common.service import BusyThread, Principal, ThreadRegistry


@pytest.mark.parametrize("approved", [True, False])
async def test_api_never_confuses_customer_access_with_adjuster_authority(approved):
    result = await exercise_api(approved, stale=True)
    assert result["created"] == 201
    assert result["foreign_status"] == 404
    assert result["customer_approval_status"] == 403
    assert result["stale_status"] == 409
    assert result["effects"] == int(approved)
    assert result["status"] == ("recorded" if approved else "not_approved")


async def test_only_one_run_per_thread_and_lease_released_on_error(tmp_path):
    registry = ThreadRegistry(tmp_path / "registry.db")
    with pytest.raises(RuntimeError):
        async with registry.guard("claim"):
            with pytest.raises(BusyThread):
                async with registry.guard("claim"):
                    pytest.fail("A second run entered the same thread")
            raise RuntimeError("Synthetic cancellation")
    async with registry.guard("claim"):
        assert registry.locks["claim"].locked()
    assert registry.locks == {}


async def test_registry_does_not_allow_claim_ownership_substitution(tmp_path):
    registry = ThreadRegistry(tmp_path / "registry.db")
    with pytest.raises(PermissionError):
        await registry.create(
            "claim", Principal("customer", "CUS-0001", "customer"), {"customer_id": "CUS-0002"}
        )


def test_idempotency_is_bound_to_the_exact_effect_payload(tmp_path):
    ledger = EffectLedger(tmp_path / "ledger.db")
    assert ledger.record("payment:claim", {"amount_cents": 100})
    assert not ledger.record("payment:claim", {"amount_cents": 100})
    with pytest.raises(ValueError, match="different payload"):
        ledger.record("payment:claim", {"amount_cents": 200})
    assert ledger.rows() == [{"key": "payment:claim", "payload": {"amount_cents": 100}}]
