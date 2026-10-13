---
id: "P3-197"
title: "Report unknown underlying capabilities without false negative guarantees"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.7", "5.6.2", "5.7.1"]
strength: "SHOULD"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.7", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1"]
---

# P3-197 - Report unknown underlying capabilities without false negative guarantees

## Rule

Where underlying write, access, execution, or user-capability information is unavailable, follow the specified permissive metadata fallback and return the real operation outcome.

## Audit

Review capability discovery and forwarding behavior; do not treat an optimistic capability flag as a guarantee that the operation will succeed.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.7](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.7)
- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
