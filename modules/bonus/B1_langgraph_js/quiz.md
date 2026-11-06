# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_typescript_state.ts using one claim from its input cases.
2. Diagnose this broken behavior: Preserve Python's inclusive fast-track boundary. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_typescript_durable.ts using one claim from its input cases.
4. Diagnose this broken behavior: Accept explicit boolean decisions and reject strings at the interrupt boundary. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_typescript_agents.ts using one claim from its input cases.
6. Diagnose this broken behavior: Respect the configured loop budget in both JavaScript agents. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. TypeScript adds static types to JavaScript; StateSchema uses Zod schemas for graph state and ReducedValue declares merges. Nodes return partial objects, await obtains a Promise result, and integer cents preserve Python parity. The JavaScript API returns state directly here; do not assume Python's v2 result wrapper exists in another language.
2. Preserve Python's inclusive fast-track boundary. Compare the normal case with the boundary fixtures and identify the first differing update.
3. JavaScript Send fans out document work, SqliteSaver retains the approval pause, and Command resumes it. The saver connection is explicitly closed. JavaScript uses camelCase options such as streamMode and returns its documented update shape; this lesson intentionally does not copy Python invocation parameters.
4. Accept explicit boolean decisions and reject strings at the interrupt boundary. Compare the normal case with the boundary fixtures and identify the first differing update.
5. The TypeScript model factory returns a scripted LangChain fake with tool calls. A manual StateGraph loop and createAgent consume the same trajectory, making their roles and call identities directly comparable. The Python gym bridge executes the selected TypeScript file in Node; it never supplies the business answer itself.
6. Respect the configured loop budget in both JavaScript agents. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
