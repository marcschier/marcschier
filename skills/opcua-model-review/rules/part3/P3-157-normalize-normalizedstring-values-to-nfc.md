---
id: "P3-157"
title: "Normalize NormalizedString values to NFC"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.45"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.45"]
---

# P3-157 - Normalize NormalizedString values to NFC

## Rule

NormalizedString values use Unicode Normalization Form C.

## Audit

Compare Unicode-normalized content rather than byte equality of visually similar text.

## Source

- [OPC 10000-3 v1.05.06, clause 8.45](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.45)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
