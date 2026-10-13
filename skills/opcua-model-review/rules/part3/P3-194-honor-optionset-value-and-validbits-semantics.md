---
id: "P3-194"
title: "Honor OptionSet Value and ValidBits semantics"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.40"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.40"]
---

# P3-194 - Honor OptionSet Value and ValidBits semantics

## Rule

OptionSet Value and ValidBits have equal byte lengths. Writes change only requested valid bits and reject invalid-bit requests without partially applying them.

## Audit

Check supplied structured values and the write contract, including preservation of unselected bits.

## Source

- [OPC 10000-3 v1.05.06, clause 8.40](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.40)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
