# Common bugs

These are observed faults in runnable starters. Each entry includes an actual counterexample, its wrong output or exception type, the cause, and the repair practiced in the linked Fix task. Run from the repository root after installing the lesson's dependencies.

## 1. Environment

**Symptom:** input `{"python": [3, 12], "packages": ["langgraph", "pytest"], "data_present": true, "live": false, "provider_ready": false}` produces:

```json
{
  "value": {
    "ready": false,
    "errors": [
      "Optional live provider is not configured"
    ],
    "mode": "offline"
  }
}
```

**Cause:** the faulty operation is `not case["provider_ready"]`. A missing provider is a problem only when live mode was requested.

**Fix:** restore `case["live"] and not case["provider_ready"]` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "ready": true,
    "errors": [],
    "mode": "offline"
  }
}
```

[Practice Fix 00-08](../gym/tasks/00/00-08_environment_fix/task.md) · [Lesson](../modules/00_setup/README.md)

## 2. First Gym

**Symptom:** input `{"claim_type": " Water ", "claim_id": "CLM-0001"}` produces:

```json
{
  "value": {
    "claim_id": "CLM-0001",
    "label": "unknown"
  }
}
```

**Cause:** the faulty operation is `value.strip()`. Labels need case normalization before comparison.

**Fix:** restore `value.strip().lower()` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "claim_id": "CLM-0001",
    "label": "water"
  }
}
```

[Practice Fix 00-14](../gym/tasks/00/00-14_first_gym_fix/task.md) · [Lesson](../modules/00_setup/README.md)

## 3. Intake Nodes

**Symptom:** input `{"claim_id": "CLM-0001", "description": "  Pipe burst  ", "amount_cents": "125000"}` produces:

```json
{
  "error": "InvalidUpdateError"
}
```

**Cause:** the faulty operation is `return str(amount)`. A graph node must return a mapping of state updates.

**Fix:** restore `return {"amount_cents": int(amount)}` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "claim_id": "CLM-0001",
    "description": "Pipe burst",
    "amount_cents": 125000
  }
}
```

[Practice Fix 01-02](../gym/tasks/01/01-02_intake_nodes_fix/task.md) · [Lesson](../modules/01_your_first_graph/README.md)

## 4. Wire Pipeline

**Symptom:** input `{"claim_id": "CLM-0001", "description": " Water leak ", "steps": []}` produces:

```json
{
  "value": {
    "claim_id": "CLM-0001",
    "description": "Water leak",
    "acknowledged": true,
    "steps": [
      "normalize",
      "acknowledge"
    ]
  }
}
```

**Cause:** the faulty operation is `graph.add_edge("normalize", "acknowledge")`. Validation must occur before acknowledging the claim.

**Fix:** restore `graph.add_edge("normalize", "validate")` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "claim_id": "CLM-0001",
    "description": "Water leak",
    "status": "ready",
    "acknowledged": true,
    "steps": [
      "normalize",
      "validate",
      "acknowledge"
    ]
  }
}
```

[Practice Fix 01-08](../gym/tasks/01/01-08_wire_pipeline_fix/task.md) · [Lesson](../modules/01_your_first_graph/README.md)

## 5. Draw And Explain

**Symptom:** input `{"claim_id": "CLM-0001", "description": "Pipe burst"}` produces:

```json
{
  "value": {
    "steps": [
      "receive",
      "validate"
    ],
    "updates": [
      {
        "receive": {
          "received": true
        }
      },
      {
        "validate": {
          "valid": true
        }
      }
    ]
  }
}
```

**Cause:** the faulty operation is `graph.add_edge("validate", END)`. The intended final node must be connected.

**Fix:** restore `graph.add_edge("validate", "acknowledge")` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "steps": [
      "receive",
      "validate",
      "acknowledge"
    ],
    "updates": [
      {
        "receive": {
          "received": true
        }
      },
      {
        "validate": {
          "valid": true
        }
      },
      {
        "acknowledge": {
          "acknowledged": true
        }
      }
    ]
  }
}
```

[Practice Fix 01-14](../gym/tasks/01/01-14_draw_and_explain_fix/task.md) · [Lesson](../modules/01_your_first_graph/README.md)

## 6. Schema Contracts

**Symptom:** input `{"kind": "pydantic", "amount_cents": 125000, "claim_id": "CLM-0001"}` produces:

```json
{
  "error": "ValueError"
}
```

**Cause:** the faulty operation is `return dict()`. Use Pydantic field access or model_dump instead of losing validated values.

**Fix:** restore `return state.model_dump()` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "output_type": "ClaimModel",
    "value": {
      "claim_id": "CLM-0001",
      "amount_cents": 125000,
      "status": "validated"
    }
  }
}
```

[Practice Fix 02-02](../gym/tasks/02/02-02_schema_contracts_fix/task.md) · [Lesson](../modules/02_state_and_reducers/README.md)

## 7. Reducer Findings

**Symptom:** input `{"first": {"id": "receipt", "severity": 1}, "second": {"id": "receipt", "severity": 3}}` produces:

```json
{
  "value": {
    "findings": [
      {
        "id": "receipt",
        "severity": 3
      }
    ],
    "log": [
      "estimate",
      "estimate",
      "receipt"
    ],
    "last": "receipt"
  }
}
```

**Cause:** the faulty operation is `"log": state["log"] + ["receipt"]`. Return new evidence only; the reducer already has previous values.

**Fix:** restore `"log": ["receipt"]` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "findings": [
      {
        "id": "receipt",
        "severity": 3
      }
    ],
    "log": [
      "estimate",
      "receipt"
    ],
    "last": "receipt"
  }
}
```

[Practice Fix 02-08](../gym/tasks/02/02-08_reducer_findings_fix/task.md) · [Lesson](../modules/02_state_and_reducers/README.md)

## 8. State Boundaries

**Symptom:** input `{"claim_id": "CLM-0001", "text": "  Pipe burst  "}` produces:

```json
{
  "value": {
    "fields": [
      "claim_id",
      "messages"
    ],
    "claim_id": "CLM-0001",
    "messages": [
      {
        "id": "customer-1",
        "content": "  Pipe burst  "
      },
      {
        "id": "customer-2",
        "content": "Pipe burst"
      }
    ]
  }
}
```

**Cause:** the faulty operation is `state["text"].strip(), id="customer-2"`. Use the same message ID to replace the original message.

**Fix:** restore `state["text"].strip(), id="customer-1"` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "fields": [
      "claim_id",
      "messages"
    ],
    "claim_id": "CLM-0001",
    "messages": [
      {
        "id": "customer-1",
        "content": "Pipe burst"
      }
    ]
  }
}
```

[Practice Fix 02-14](../gym/tasks/02/02-14_state_boundaries_fix/task.md) · [Lesson](../modules/02_state_and_reducers/README.md)

## 9. Conditional Router

**Symptom:** input `{"claim_type": "water", "amount_cents": 100000, "missing": []}` produces:

```json
{
  "value": {
    "claim_type": "water",
    "amount_cents": 100000,
    "missing": [],
    "route": "specialist"
  }
}
```

**Cause:** the faulty operation is `{label: "specialist" for label in destinations}`. Path-map values must match each intended destination.

**Fix:** restore `{label: label for label in destinations}` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "claim_type": "water",
    "amount_cents": 100000,
    "missing": [],
    "route": "fast_track"
  }
}
```

[Practice Fix 03-02](../gym/tasks/03/03-02_conditional_router_fix/task.md) · [Lesson](../modules/03_branching_and_routing/README.md)

## 10. Command Routes

**Symptom:** input `{"claim_id": "CLM-0001", "suspicious": true}` produces:

```json
{
  "value": {
    "claim_id": "CLM-0001",
    "suspicious": true,
    "reason": "indicator",
    "visited": [
      "acknowledge",
      "review"
    ]
  }
}
```

**Cause:** the faulty operation is `graph.add_edge(START, "triage")
    graph.add_edge("triage", "acknowledge")`. A competing static edge schedules an extra acknowledgment.

**Fix:** restore `graph.add_edge(START, "triage")` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "claim_id": "CLM-0001",
    "suspicious": true,
    "reason": "indicator",
    "visited": [
      "review"
    ]
  }
}
```

[Practice Fix 03-08](../gym/tasks/03/03-08_command_routes_fix/task.md) · [Lesson](../modules/03_branching_and_routing/README.md)

## 11. Early Exit

**Symptom:** input `{"claim_id": "CLM-0001", "amount_cents": 0, "duplicate_of": null}` produces:

```json
{
  "value": {
    "claim_id": "CLM-0001",
    "amount_cents": 0,
    "duplicate_of": null,
    "reason": "invalid",
    "assigned": false
  }
}
```

**Cause:** the faulty operation is `amount <= 0`. Zero is a defined boundary, not an omitted case.

**Fix:** restore `amount < 0` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "claim_id": "CLM-0001",
    "amount_cents": 0,
    "duplicate_of": null,
    "reason": "eligible",
    "assigned": true
  }
}
```

[Practice Fix 03-14](../gym/tasks/03/03-14_early_exit_fix/task.md) · [Lesson](../modules/03_branching_and_routing/README.md)

## 12. Bounded Rechecks

**Symptom:** input `{"history": [false, false, true], "budget": 3}` produces:

```json
{
  "error": "GraphRecursionError"
}
```

**Cause:** the faulty operation is `"attempts": index`. Without a changing retry counter, the graph reaches its recursion limit.

**Fix:** restore `"attempts": index + 1` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "history": [
      false,
      false,
      true
    ],
    "budget": 3,
    "attempts": 3,
    "status": "ready",
    "trace": [
      "missing",
      "missing",
      "received"
    ]
  }
}
```

[Practice Fix 04-02](../gym/tasks/04/04-02_bounded_rechecks_fix/task.md) · [Lesson](../modules/04_loops_parallel_map_reduce/README.md)

## 13. Fan Out Fan In

**Symptom:** input `{"documents": [{"id": "DOC-001", "kind": "estimate"}, {"id": "DOC-021", "kind": "police"}]}` produces:

```json
{
  "value": {
    "findings": [
      "DOC-021"
    ],
    "summaries": [
      [
        "DOC-021"
      ]
    ]
  }
}
```

**Cause:** the faulty operation is `findings: list[str]`. Parallel writes to an overwrite channel conflict.

**Fix:** restore `findings: Annotated[list[str], operator.add]` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "findings": [
      "DOC-001",
      "DOC-021"
    ],
    "summaries": [
      [
        "DOC-001",
        "DOC-021"
      ]
    ]
  }
}
```

[Practice Fix 04-08](../gym/tasks/04/04-08_fan_out_fan_in_fix/task.md) · [Lesson](../modules/04_loops_parallel_map_reduce/README.md)

## 14. Retry And Cache

**Symptom:** input `{"customer_id": "CUS-0001", "policy_version": 1, "amount_cents": 125000, "ttl": 10, "advance": 10}` produces:

```json
{
  "value": {
    "covered": [
      true,
      true,
      true,
      true
    ],
    "lookup_calls": 3
  }
}
```

**Cause:** the faulty operation is `[state["policy_version"], state["amount_cents"]]`. Customer identity belongs in the cache key.

**Fix:** restore `[state["customer_id"], state["policy_version"], state["amount_cents"]]` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "covered": [
      true,
      true,
      true,
      false
    ],
    "lookup_calls": 4
  }
}
```

[Practice Fix 04-14](../gym/tasks/04/04-14_retry_and_cache_fix/task.md) · [Lesson](../modules/04_loops_parallel_map_reduce/README.md)

## 15. Thread Identity

**Symptom:** input `{"first_id": "CLM-0001", "second_id": "CLM-0002"}` produces:

```json
{
  "error": "ValueError"
}
```

**Cause:** the faulty operation is `{}`. A persisted invocation needs an explicit thread identifier.

**Fix:** restore `{"thread_id": "claim:" + claim_id}` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "first_notes": [
      "received",
      "estimate attached"
    ],
    "second_notes": [
      "other customer"
    ]
  }
}
```

[Practice Fix 05-02](../gym/tasks/05/05-02_thread_identity_fix/task.md) · [Lesson](../modules/05_persistence_and_threads/README.md)

## 16. Sqlite Lifetime

**Symptom:** input `{"claim_id": "CLM-0001"}` produces:

```json
{
  "error": "JSONDecodeError"
}
```

**Cause:** the faulty operation is `with SqliteSaver.from_conn_string(database) as saver:
        graph = build_graph(saver)
    result = graph.invoke(payload, config, version="v2").value`. A compiled graph cannot use a saver whose connection has closed.

**Fix:** restore `with SqliteSaver.from_conn_string(database) as saver:
        result = build_graph(saver).invoke(payload, config, version="v2").value` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "first_notes": [
      "received"
    ],
    "second_notes": [
      "received",
      "estimate attached"
    ],
    "closed": true
  }
}
```

[Practice Fix 05-08](../gym/tasks/05/05-08_sqlite_lifetime_fix/task.md) · [Lesson](../modules/05_persistence_and_threads/README.md)

## 17. Inspect Checkpoints

**Symptom:** input `{"amount_cents": 100000, "corrected_amount": 200000, "durability": "sync"}` produces:

```json
{
  "value": {
    "original": "fast_track",
    "corrected": "fast_track",
    "pending_after_edit": [
      "decide"
    ],
    "parent_exists": true,
    "saved_steps": [
      -1,
      0,
      1,
      2
    ]
  }
}
```

**Cause:** the faulty operation is `graph.invoke(None, history[-1].config, version="v2")`. Continue the configuration returned by update_state, not an unrelated checkpoint.

**Fix:** restore `graph.invoke(None, corrected, version="v2")` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "original": "fast_track",
    "corrected": "standard",
    "pending_after_edit": [
      "decide"
    ],
    "parent_exists": true,
    "saved_steps": [
      -1,
      0,
      1,
      2
    ]
  }
}
```

[Practice Fix 05-14](../gym/tasks/05/05-14_inspect_checkpoints_fix/task.md) · [Lesson](../modules/05_persistence_and_threads/README.md)

## 18. Approve Or Reject

**Symptom:** input `{"amount_cents": 600000, "decision": {"approved": true}}` produces:

```json
{
  "error": "RuntimeError"
}
```

**Cause:** the faulty operation is `checkpointer=None`. An interrupt needs persistence to resume the saved task.

**Fix:** restore `checkpointer=InMemorySaver()` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "prompts": [
      {
        "kind": "payout_review",
        "amount_cents": 600000
      }
    ],
    "status": "approved",
    "remaining": 0
  }
}
```

[Practice Fix 06-02](../gym/tasks/06/06-02_approve_or_reject_fix/task.md) · [Lesson](../modules/06_human_in_the_loop/README.md)

## 19. Collect And Edit

**Symptom:** input `{"loss_date": "2026-01-01", "approved_cents": 125000}` produces:

```json
{
  "error": "ValueError"
}
```

**Cause:** the faulty operation is `case["loss_date"]`. Each interrupt must receive the response for its own request kind.

**Fix:** restore `case[item.value["kind"]]` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "prompts": [
      "approved_cents",
      "loss_date"
    ],
    "result": {
      "claim_id": "CLM-0001",
      "loss_date": "2026-01-01",
      "approved_cents": 125000
    }
  }
}
```

[Practice Fix 06-08](../gym/tasks/06/06-08_collect_and_edit_fix/task.md) · [Lesson](../modules/06_human_in_the_loop/README.md)

## 20. Safe Reentry

**Symptom:** input `{"claim_id": "CLM-0001", "approved": true}` produces:

```json
{
  "value": {
    "entries": 2,
    "before_approval": 1,
    "notifications": 3,
    "approved": true
  }
}
```

**Cause:** the faulty operation is `entries.append("review")
        notifications[str(len(entries))] = "Premature notification"`. Effects before interrupt repeat when the node restarts.

**Fix:** restore `entries.append("review")` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "entries": 2,
    "before_approval": 0,
    "notifications": 1,
    "approved": true
  }
}
```

[Practice Fix 06-14](../gym/tasks/06/06-14_safe_reentry_fix/task.md) · [Lesson](../modules/06_human_in_the_loop/README.md)

## 21. Replay And Fork

**Symptom:** input `{"amount_cents": 100000, "corrected_amount": 600000}` produces:

```json
{
  "value": {
    "original_route": "fast_track",
    "fork_route": "fast_track",
    "replay_prompts": 1,
    "fork_prompts": 1,
    "original_unchanged": true,
    "fork_parent_is_historical": true
  }
}
```

**Cause:** the faulty operation is `graph.invoke(None, historical.config, version="v2")`. Replay the new fork configuration, not its uncorrected parent.

**Fix:** restore `graph.invoke(None, fork_config, version="v2")` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "original_route": "fast_track",
    "fork_route": "specialist",
    "replay_prompts": 1,
    "fork_prompts": 1,
    "original_unchanged": true,
    "fork_parent_is_historical": true
  }
}
```

[Practice Fix 07-02](../gym/tasks/07/07-02_replay_and_fork_fix/task.md) · [Lesson](../modules/07_time_travel_and_streaming/README.md)

## 22. V2 Stream Parts

**Symptom:** input `{"claim_id": "CLM-0001", "review": false}` produces:

```json
{
  "value": {
    "parts": [
      {
        "type": "debug",
        "namespace": [],
        "event": "checkpoint"
      },
      {
        "type": "values",
        "namespace": [],
        "status": "input",
        "interrupts": 0
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "checkpoint"
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "task"
      },
      {
        "type": "custom",
        "namespace": [],
        "phase": "received"
      },
      {
        "type": "updates",
        "namespace": [],
        "nodes": [
          "receive"
        ]
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "task_result"
      },
      {
        "type": "values",
        "namespace": [],
        "status": "input",
        "interrupts": 0
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "checkpoint"
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "task"
      },
      {
        "type": "updates",
        "namespace": [],
        "nodes": [
          "validate"
        ]
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "task_result"
      },
      {
        "type": "values",
        "namespace": [],
        "status": "input",
        "interrupts": 0
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "checkpoint"
      }
    ]
  }
}
```

**Cause:** the faulty operation is `part.get("status", "input")`. The state payload is inside data, not at the envelope root.

**Fix:** restore `part["data"].get("status", "input")` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "parts": [
      {
        "type": "debug",
        "namespace": [],
        "event": "checkpoint"
      },
      {
        "type": "values",
        "namespace": [],
        "status": "input",
        "interrupts": 0
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "checkpoint"
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "task"
      },
      {
        "type": "custom",
        "namespace": [],
        "phase": "received"
      },
      {
        "type": "updates",
        "namespace": [],
        "nodes": [
          "receive"
        ]
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "task_result"
      },
      {
        "type": "values",
        "namespace": [],
        "status": "received",
        "interrupts": 0
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "checkpoint"
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "task"
      },
      {
        "type": "updates",
        "namespace": [],
        "nodes": [
          "validate"
        ]
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "task_result"
      },
      {
        "type": "values",
        "namespace": [],
        "status": "validated",
        "interrupts": 0
      },
      {
        "type": "debug",
        "namespace": [],
        "event": "checkpoint"
      }
    ]
  }
}
```

[Practice Fix 07-08](../gym/tasks/07/07-08_v2_stream_parts_fix/task.md) · [Lesson](../modules/07_time_travel_and_streaming/README.md)

## 23. Namespaces And Errors

**Symptom:** input `{"claim_id": "CLM-0001"}` produces:

```json
{
  "value": {
    "groups": {
      "document_review": [
        "check_document"
      ],
      "parent": [
        "check_identity",
        "document_review",
        "summarize"
      ]
    },
    "summary_last": false
  }
}
```

**Cause:** the faulty operation is `if part["ns"]`. Keep parent and child scopes distinct.

**Fix:** restore `if not part["ns"]` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "groups": {
      "document_review": [
        "check_document"
      ],
      "parent": [
        "check_identity",
        "document_review",
        "summarize"
      ]
    },
    "summary_last": true
  }
}
```

[Practice Fix 07-14](../gym/tasks/07/07-14_namespaces_and_errors_fix/task.md) · [Lesson](../modules/07_time_travel_and_streaming/README.md)

## 24. Model Boundary

**Symptom:** input `{"claim_type": "water", "amount_cents": 100000, "confidence": 0.9}` produces:

```json
{
  "value": {
    "facts": {
      "claim_type": "water",
      "amount_cents": 100000,
      "loss_date": null,
      "confidence": 0.9
    },
    "route": "standard"
  }
}
```

**Cause:** the faulty operation is `facts.amount_cents < 100000`. Include exactly 100000 cents in fast-track routing.

**Fix:** restore `facts.amount_cents <= 100000` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "facts": {
      "claim_type": "water",
      "amount_cents": 100000,
      "loss_date": null,
      "confidence": 0.9
    },
    "route": "fast_track"
  }
}
```

[Practice Fix 08-02](../gym/tasks/08/08-02_model_boundary_fix/task.md) · [Lesson](../modules/08_llms_inside_nodes/README.md)

## 25. Message Identity

**Symptom:** input `{"text": "Corrected: pipe burst", "remove_customer": true}` produces:

```json
{
  "error": "AttributeError"
}
```

**Cause:** the faulty operation is `HumanMessage(content=case["text"], id="customer-2")`. Correct an existing message without appending another customer message.

**Fix:** restore `HumanMessage(content=case["text"], id="customer-1")` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "messages": [
      {
        "role": "ai",
        "id": "agent-1",
        "text": ""
      },
      {
        "role": "tool",
        "id": "tool-1",
        "text": "Synthetic policy found"
      }
    ],
    "paired": true
  }
}
```

[Practice Fix 08-08](../gym/tasks/08/08-08_message_identity_fix/task.md) · [Lesson](../modules/08_llms_inside_nodes/README.md)

## 26. Tokens And Fakes

**Symptom:** input `{"text": "Larkspur received your synthetic claim.", "structured": false}` produces:

```json
{
  "error": "KeyError"
}
```

**Cause:** the faulty operation is `metadata["missing_node"]`. Read the documented node name from stream metadata.

**Fix:** restore `metadata["langgraph_node"]` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "text": "Larkspur received your synthetic claim.",
    "matches_invoke": true,
    "structured": null,
    "nodes": [
      "acknowledge"
    ],
    "nonempty_chunks": 5
  }
}
```

[Practice Fix 08-14](../gym/tasks/08/08-14_tokens_and_fakes_fix/task.md) · [Lesson](../modules/08_llms_inside_nodes/README.md)

## 27. Tools And Messages

**Symptom:** input `{"policy_id": "MISSING", "amount_cents": 125000}` produces:

```json
{
  "error": "ValueError"
}
```

**Cause:** the faulty operation is `handle_tool_errors=False`. Return a correlated tool error for an unknown policy.

**Fix:** restore `handle_tool_errors=True` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "results": [
      {
        "call_id": "payout-call",
        "status": "success",
        "content": "25000"
      },
      {
        "call_id": "policy-call",
        "status": "error",
        "content": "Error: ValueError('Unknown synthetic policy')\n Please fix your mistakes."
      }
    ]
  }
}
```

[Practice Fix 09-02](../gym/tasks/09/09-02_tools_and_messages_fix/task.md) · [Lesson](../modules/09_tools_and_agent_loop/README.md)

## 28. Manual React

**Symptom:** input `{"policy_id": "MISSING", "recursion_limit": 12}` produces:

```json
{
  "error": "ValueError"
}
```

**Cause:** the faulty operation is `handle_tool_errors=False`. Let the agent observe a policy lookup failure.

**Fix:** restore `handle_tool_errors=True` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "roles": [
      "human",
      "ai",
      "tool",
      "ai"
    ],
    "tool_results": [
      "Error: ValueError('Unknown policy')\n Please fix your mistakes."
    ],
    "final": "Use the tool result as evidence; this is not payment approval."
  }
}
```

[Practice Fix 09-08](../gym/tasks/09/09-08_manual_react_fix/task.md) · [Lesson](../modules/09_tools_and_agent_loop/README.md)

## 29. Tool Runtime

**Symptom:** input `{"customer_id": "CUS-0001", "preference": "email"}` produces:

```json
{
  "value": {
    "saved": {
      "value": "email"
    },
    "state_preference": "phone",
    "tool_call_id": "save-1",
    "model_visible_fields": [
      "preference"
    ]
  }
}
```

**Cause:** the faulty operation is `"saved_preference": "phone"`. Keep the graph state consistent with the Store write.

**Fix:** restore `"saved_preference": preference` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "saved": {
      "value": "email"
    },
    "state_preference": "email",
    "tool_call_id": "save-1",
    "model_visible_fields": [
      "preference"
    ]
  }
}
```

[Practice Fix 09-14](../gym/tasks/09/09-14_tool_runtime_fix/task.md) · [Lesson](../modules/09_tools_and_agent_loop/README.md)

## 30. Create Agent

**Symptom:** input `{"policy_id": "POL-0001"}` produces:

```json
{
  "error": "ValueError"
}
```

**Cause:** the faulty operation is `if policy_id == "POL-0001":`. Reject unknown policy IDs, not the known fixture.

**Fix:** restore `if policy_id != "POL-0001":` and compare every declared case. The required result for this counterexample is:

```json
{
  "value": {
    "roles": [
      "human",
      "ai",
      "tool",
      "ai"
    ],
    "tools": [
      "lookup_policy"
    ],
    "final": "A policy lookup is evidence, not payout authorization."
  }
}
```

[Practice Fix 10-02](../gym/tasks/10/10-02_create_agent_fix/task.md) · [Lesson](../modules/10_prebuilt_agents/README.md)
