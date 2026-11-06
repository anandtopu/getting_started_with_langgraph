# Concepts used for the first time

You only need basic Python before starting. Read each short section when its module introduces the concept, then return to the runnable example.

## Testing — module 00

A test calls your code with an input and checks a requirement with `assert`. A failed assertion means the observed result differs from that requirement. It does not necessarily mean Python failed to run. `pytest` discovers functions named `test_...`; the gym runs those functions against your selected workspace file.

```python
def normalize(label):
    return label.strip().lower()


def test_normalize():
    assert normalize(" WATER ") == "water"
```

A syntax/import error prevents a test from reaching its assertion. A skipped test supplies no evidence. Predict and Trace exercises grade written JSON. Refactor exercises keep the original behavior tests green and add a structural check. Extend exercises retain the old contract and add tests for the new capability.

## State and type hints — modules 01–02

State is the data carried between steps. A `TypedDict` describes keys for readers and type checkers; it does **not** validate values at runtime. Returning `{"route": "review"}` from a node changes that field while preserving other fields. A reducer defines how two writes to the same field combine.

Pydantic performs runtime validation. A model is a class describing acceptable input, not an AI model. For example, `StrictInt` rejects `True` and `"100"` even though Python can convert them to integers. Validation can reject a missing field; it cannot discover the correct missing fact. Route incomplete submissions to an information-request path before trying to parse a complete extraction schema.

## Workflows and agents — modules 00 and 09–10

A workflow follows transitions you define. An agent uses model output to select tools within the choices you expose. A state machine names states and allowed transitions. LangGraph adds persistent execution and shared state to this style of programming; it does not decide your business rules.

## Language models and messages — module 08

A chat model predicts an output from messages. Messages have roles: human input, AI output, system instructions, and tool results. Tokens are pieces of text processed by the model, not always whole words. A context window limits the amount it can process in a request. A scripted fake supplies predetermined messages and proves your program handles them; it does not measure how well a real model understands a claim.

Structured output asks for an agreed schema. Still validate and check evidence before using those fields. The [provider lab](LIVE_MODEL_LAB.md) compares real inference with the deterministic examples after you finish the offline lesson.

## Tool calls — module 09

A tool call is a proposed function name, arguments, and call ID in an AI message. It is not the function execution itself. Your application validates permission and arguments, executes the selected function, then returns a `ToolMessage` with the matching call ID. A policy-reading tool should not also issue payments. Treat customer text and model output as untrusted data rather than authority.

## Async Python — modules 16 and 18

An `async def` function returns a coroutine when called. `await` lets other work run while that coroutine waits for I/O. It does not make blocking database calls nonblocking by itself. `asyncio.run(main())` starts an event loop in a normal script; do not start another loop inside an already running one.

An async generator uses `yield` to produce multiple items; consume it with `async for`. A streaming response keeps producing events until it completes, pauses, errors, or is cancelled. Put cleanup in `finally`/context managers and propagate cancellation so locks and connections are released. The module notebooks launch the canonical script in a child process to avoid nested event loops.

## Persistence and replay — modules 05–07

A thread identifies a sequence of saved states. A checkpoint records a boundary of execution, including pending work. Resuming a stopped run uses that saved work. Replaying a historical checkpoint executes work after that earlier boundary again. Invoking a completed checkpoint with no input may do no work; that alone does not test replay. External effects require their own stable idempotency keys.

Validate a human response **before** submitting `Command(resume=...)`: a saved invalid response may be replayed on every retry. An HTTP request that fails validation should leave the interrupt available for correction. Replaying before an approval can ask the human again.
