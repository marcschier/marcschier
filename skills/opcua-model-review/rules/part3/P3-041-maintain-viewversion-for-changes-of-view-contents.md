---
id: "P3-041"
title: "Maintain ViewVersion for changes of View contents"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.4", "9.32.3"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.3"]
---

# P3-041 - Maintain ViewVersion for changes of View contents

## Rule

A supplied ViewVersion is greater than zero and changes when View contents change, including changes below directly referenced members.

## Audit

Review the version Property and update/event contract. ViewVersion is optional when a Server cannot detect such changes.

## Source

- [OPC 10000-3 v1.05.06, clause 5.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4)
- [OPC 10000-3 v1.05.06, clause 9.32.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
