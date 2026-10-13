---
id: "P3-009"
title: "Assign unique non-null NodeIds"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.2", "8.2.1", "8.2.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "identity"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.4"]
---

# P3-009 - Assign unique non-null NodeIds

## Rule

Each Node has an unambiguous canonical NodeId and cannot use any of the defined null NodeId forms.

## Audit

Compare namespace-URI-qualified identifiers, including numeric, string, GUID, and opaque null representations. Deduplicate the same dependency definition rather than treating a repeated import as a new Node.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.2)
- [OPC 10000-3 v1.05.06, clause 8.2.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.1)
- [OPC 10000-3 v1.05.06, clause 8.2.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
