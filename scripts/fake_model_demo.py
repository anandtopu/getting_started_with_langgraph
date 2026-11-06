"""Exercise scripted text, structured extraction, and token streaming.

Run: uv run python scripts/fake_model_demo.py
Expected: a received-claim message, water/125000 extraction, and streamed text.
LLM: optional. Default fake mode costs $0; --live uses the configured provider.
Synthetic data only. Never use a model response as payout authorization.
"""

import argparse

from common.config import ConfigurationError
from common.models import get_chat_model
from common.pretty import print_state
from common.schemas import ClaimExtraction


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true")
    arguments = parser.parse_args()
    mode = "live" if arguments.live else "fake"
    try:
        model = get_chat_model(mode=mode)
        print_state(
            model.invoke("Acknowledge this fictional Larkspur claim.").content, title="Text"
        )
        model = get_chat_model(mode=mode, scenario="extract")
        extraction = model.with_structured_output(ClaimExtraction).invoke(
            "Extract: a pipe burst on 2026-01-15; claimed amount is $1,250. Confidence 1.0."
        )
        print_state(extraction, title="Validated extraction")
        text = "".join(
            str(chunk.content)
            for chunk in get_chat_model(mode=mode).stream("Acknowledge the claim.")
        )
        print_state(text, title="Streamed text")
    except ConfigurationError as error:
        raise SystemExit(str(error)) from None
    except Exception:
        if not arguments.live:
            raise
        raise SystemExit(
            "The optional live call failed. Check provider access, model capabilities, and service status "
            "with uv run python scripts/check_env.py --live. No key values are displayed."
        ) from None


if __name__ == "__main__":
    main()
