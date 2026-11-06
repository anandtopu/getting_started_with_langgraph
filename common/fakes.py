"""Scripted LangChain fake models: no cycling, network, or provider keys."""

import json
import re
from collections.abc import Iterator, Sequence
from threading import Lock
from typing import Any

from langchain_core.language_models.fake_chat_models import FakeMessagesListChatModel
from langchain_core.messages import AIMessage, AIMessageChunk, BaseMessage
from langchain_core.outputs import ChatGeneration, ChatGenerationChunk, ChatResult
from langchain_core.runnables import RunnableLambda
from langchain_core.utils.function_calling import convert_to_openai_tool
from pydantic import BaseModel, PrivateAttr


class ScriptExhaustedError(RuntimeError):
    """The fake received more model calls than its scenario specifies."""


class ScriptedChatModel(FakeMessagesListChatModel):
    """Extend LangChain's fake with tool binding, structured output, and streaming.

    Each instance owns its cursor. Share neither an instance nor a cursor between
    tests; concurrent callers should use independent scripted models.
    """

    temperature: float = 0
    _lock: Lock = PrivateAttr(default_factory=Lock)
    _history: list[list[BaseMessage]] = PrivateAttr(default_factory=list)

    @property
    def calls(self) -> int:
        return self.i

    @property
    def history(self) -> list[list[BaseMessage]]:
        return [[message.model_copy(deep=True) for message in call] for call in self._history]

    def reset(self) -> None:
        with self._lock:
            self.i = 0
            self._history.clear()

    def _generate(
        self,
        messages: list[BaseMessage],
        stop: list[str] | None = None,
        run_manager: Any = None,
        **kwargs: Any,
    ) -> ChatResult:
        with self._lock:
            if self.i >= len(self.responses):
                raise ScriptExhaustedError(
                    "The scripted model ran out of responses; inspect the agent loop."
                )
            response = self.responses[self.i].model_copy(deep=True)
            if not isinstance(response, AIMessage):
                raise TypeError("Scripted responses must be AIMessage instances.")
            if response.id is None:
                response.id = f"scripted-{self.i + 1}"
            bound_names = {tool["function"]["name"] for tool in kwargs.get("tools", [])}
            if "tools" in kwargs and any(
                call["name"] not in bound_names for call in response.tool_calls
            ):
                raise ValueError("The script requested a tool that is not bound to this model.")
            self._history.append([message.model_copy(deep=True) for message in messages])
            self.i += 1
        return ChatResult(generations=[ChatGeneration(message=response)])

    def bind_tools(
        self, tools: Sequence[Any], *, tool_choice: str | None = None, **kwargs: Any
    ) -> Any:
        formatted = [convert_to_openai_tool(tool) for tool in tools]
        return self.bind(tools=formatted, tool_choice=tool_choice, **kwargs)

    def with_structured_output(
        self, schema: dict[str, Any] | type, *, include_raw: bool = False, **kwargs: Any
    ) -> Any:
        if not isinstance(schema, type) or not issubclass(schema, BaseModel):
            raise TypeError("Course structured-output fakes use a Pydantic model schema.")

        def parse(message: AIMessage) -> Any:
            try:
                value = schema.model_validate(
                    message.tool_calls[0]["args"]
                    if message.tool_calls
                    else json.loads(str(message.content))
                )
            except (ValueError, TypeError) as error:
                if include_raw:
                    return {"raw": message, "parsed": None, "parsing_error": error}
                raise
            return (
                {"raw": message, "parsed": value, "parsing_error": None} if include_raw else value
            )

        return self | RunnableLambda(parse)

    def _stream(
        self,
        messages: list[BaseMessage],
        stop: list[str] | None = None,
        run_manager: Any = None,
        **kwargs: Any,
    ) -> Iterator[ChatGenerationChunk]:
        message = self._generate(messages, stop=stop, **kwargs).generations[0].message
        if not isinstance(message.content, str):
            raise TypeError("The course fake streams text content, not multimodal content.")
        for token in re.findall(r"\S+\s*|\s+", message.content):
            yield ChatGenerationChunk(message=AIMessageChunk(content=token, id=message.id))
        for index, call in enumerate(message.tool_calls):
            arguments = json.dumps(call["args"], sort_keys=True)
            split = max(1, len(arguments) // 2)
            for offset, part in enumerate((arguments[:split], arguments[split:])):
                yield ChatGenerationChunk(
                    message=AIMessageChunk(
                        content="",
                        id=message.id,
                        tool_call_chunks=[
                            {
                                "name": call["name"] if offset == 0 else None,
                                "id": call["id"] if offset == 0 else None,
                                "args": part,
                                "index": index,
                            }
                        ],
                    )
                )
        yield ChatGenerationChunk(
            message=AIMessageChunk(content="", id=message.id, chunk_position="last")
        )


def scripted_scenario(name: str) -> list[AIMessage]:
    """Return a fresh scenario; arbitrary test scripts can also be supplied by callers."""
    if name == "acknowledge":
        return [AIMessage(content="Larkspur received your synthetic claim.", id="ack-1")]
    if name == "extract":
        return [
            AIMessage(
                content=json.dumps(
                    {
                        "claim_type": "water",
                        "amount_cents": 125_000,
                        "loss_date": "2026-01-15",
                        "confidence": 1.0,
                    }
                ),
                id="extraction-1",
            )
        ]
    if name == "policy_lookup":
        return [
            AIMessage(
                content="",
                id="lookup-1",
                tool_calls=[
                    {
                        "name": "lookup_policy",
                        "args": {"policy_id": "POL-0001"},
                        "id": "call-policy-1",
                        "type": "tool_call",
                    }
                ],
            ),
            AIMessage(content="The synthetic home policy has a $1,000 deductible.", id="answer-1"),
        ]
    raise ValueError(f"Unknown offline scenario: {name}")
