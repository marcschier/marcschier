---
id: "P3-176"
title: "Use complete non-redundant ModelChange event summaries"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["9.32.4", "9.32.7"]
strength: "SHOULD"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.7"]
---

# P3-176 - Use complete non-redundant ModelChange event summaries

## Rule

Prefer one event per update/group in a context; a GeneralModelChangeEvent array identifies all changes since the preceding event. Consumers handle BaseModelChangeEvent subtypes.

## Audit

Review change batching and array completeness. Event compression is permitted, so per-edit event counts are not a universal MUST.

## Source

- [OPC 10000-3 v1.05.06, clause 9.32.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.4)
- [OPC 10000-3 v1.05.06, clause 9.32.7](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.7)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
