"""Initialize every optional provider with synthetic keys; never call a model."""

import os
import sys
from unittest.mock import patch

from common.config import PROVIDERS, load_settings
from common.models import get_chat_model
from common.offline import block_network, install_socketpair_compatibility


def main() -> None:
    # Initialization is the subject of this probe. The audit guard still forbids
    # real connections, including accidental calls made by an SDK constructor.
    os.environ.pop("LARKSPUR_OFFLINE", None)
    os.environ["LANGSMITH_TRACING"] = "false"
    os.environ["LANGCHAIN_TRACING_V2"] = "false"
    install_socketpair_compatibility()
    sys.addaudithook(block_network)
    for provider in PROVIDERS:
        settings = load_settings(
            environ={
                "LLM_PROVIDER": provider,
                "OPENAI_API_KEY": "synthetic-not-a-real-key",
                "ANTHROPIC_API_KEY": "synthetic-not-a-real-key",
                "GOOGLE_API_KEY": "synthetic-not-a-real-key",
            }
        )
        with patch("common.models.check_ollama"):
            model = get_chat_model(mode="live", settings=settings)
        assert callable(model.invoke)
        assert callable(model.bind_tools)
        print(f"{provider}: {type(model).__name__} initialized; no inference requested.")
    print(
        "All four provider constructors passed. Live connectivity and model access remain untested."
    )


if __name__ == "__main__":
    main()
