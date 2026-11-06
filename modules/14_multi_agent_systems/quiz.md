# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_supervisor_tools.py using one claim from its input cases.
2. Diagnose this broken behavior: Keep specialist roles attached to the evidence they reviewed. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_handoffs.py using one claim from its input cases.
4. Diagnose this broken behavior: Pair the handoff acknowledgment with its AI request. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_team_tradeoffs.py using one claim from its input cases.
6. Diagnose this broken behavior: Advance to the next specialist instead of handing work back to itself. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. A supervisor may call specialists as tools. Each specialist gets a narrow evidence prompt and a private message history; the supervisor receives only the returned conclusion. This direct create_agent pattern avoids an extra helper package. More agents add calls and failure boundaries, so compare them against a single-agent baseline.
2. Keep specialist roles attached to the evidence they reviewed. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Command.PARENT transfers control from a child graph to a node in its parent. The shared messages channel uses add_messages. A tool-based handoff includes both the AI request and its ToolMessage acknowledgment so the next specialist receives a valid conversation. Parent destinations must not be declared as local child nodes.
4. Pair the handoff acknowledgment with its AI request. Compare the normal case with the boundary fixtures and identify the first differing update.
5. A swarm-style team routes according to the active specialist, without requiring a central supervisor on every transition. Its business budget is distinct from the graph recursion limit. This controlled four-role comparison measures calls and completion; scripted answers do not establish that the team is smarter than the one-call baseline.
6. Advance to the next specialist instead of handing work back to itself. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
