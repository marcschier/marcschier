---
id: "P3-165"
title: "Honor the access-restriction flag semantics"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.11", "8.56"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.11", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.56"]
---

# P3-165 - Honor the access-restriction flag semantics

## Rule

Apply signing, encryption, Session, and browse restriction flags according to their definitions, including the exception for Browse unless ApplyRestrictionsToBrowse is set.

## Audit

Review the access contract and runtime evidence; a flag does not by itself prove enforcement.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.11](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.11)
- [OPC 10000-3 v1.05.06, clause 8.56](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.56)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
