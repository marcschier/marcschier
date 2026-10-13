---
id: "P3-155"
title: "Encode special localized-text locales correctly"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.5.2.1", "8.5.2.2", "8.5.2.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.5.2.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.5.2.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.5.2.3"]
---

# P3-155 - Encode special localized-text locales correctly

## Rule

The mul/qst locales carry the required JSON text/replacement structures and are not Server default locales. Replacement keys are unique, non-overlapping substrings, and are not reapplied recursively.

## Audit

Review JSON keys t/r and replacement ordering/language alignment. Minified JSON is recommended, not required.

## Source

- [OPC 10000-3 v1.05.06, clause 8.5.2.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.5.2.1)
- [OPC 10000-3 v1.05.06, clause 8.5.2.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.5.2.2)
- [OPC 10000-3 v1.05.06, clause 8.5.2.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.5.2.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
