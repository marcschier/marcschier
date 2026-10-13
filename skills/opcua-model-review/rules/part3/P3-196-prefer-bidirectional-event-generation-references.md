---
id: "P3-196"
title: "Prefer bidirectional Event generation References"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.5.2", "5.6.5", "5.7.1"]
strength: "SHOULD"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1"]
---

# P3-196 - Prefer bidirectional Event generation References

## Rule

Expose GeneratesEvent in both directions where the Server can expose the inverse mapping.

## Audit

Review runtime browse directions; a unidirectional link is allowed when the inverse cannot be exposed.

## Source

- [OPC 10000-3 v1.05.06, clause 5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2)
- [OPC 10000-3 v1.05.06, clause 5.6.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5)
- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
