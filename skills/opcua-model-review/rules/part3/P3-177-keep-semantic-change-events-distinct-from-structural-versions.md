---
id: "P3-177"
title: "Keep semantic change events distinct from structural versions"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["9.33.1", "9.33.2", "9.33.3", "9.33.4"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.33.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.33.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.33.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.33.4"]
---

# P3-177 - Keep semantic change events distinct from structural versions

## Rule

SemanticChangeEvents identify the parent of a changed semantic Property; their publication does not itself update NodeVersion or ViewVersion.

## Audit

Review property flags, affected-node/type fields, View contexts, and permitted compression.

## Source

- [OPC 10000-3 v1.05.06, clause 9.33.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.33.1)
- [OPC 10000-3 v1.05.06, clause 9.33.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.33.2)
- [OPC 10000-3 v1.05.06, clause 9.33.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.33.3)
- [OPC 10000-3 v1.05.06, clause 9.33.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.33.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
