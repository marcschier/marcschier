---
id: "P3-202"
title: "Treat NodeVersion contents as opaque equality tokens"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.3"]
strength: "MUST NOT"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3"]
---

# P3-202 - Treat NodeVersion contents as opaque equality tokens

## Rule

Clients do not interpret NodeVersion contents programmatically beyond equality comparisons.

## Audit

Review client-facing version semantics; a human-readable token is not a contract for ordered or semantic-version comparisons.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
