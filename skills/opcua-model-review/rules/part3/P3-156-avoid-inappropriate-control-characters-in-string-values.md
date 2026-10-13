---
id: "P3-156"
title: "Avoid inappropriate control characters in String values"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.31"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.31"]
---

# P3-156 - Avoid inappropriate control characters in String values

## Rule

String values avoid C0/C1 controls other than whitespace.

## Audit

Check decoded String contents; identifier-specific prohibitions are stricter and remain separate.

## Source

- [OPC 10000-3 v1.05.06, clause 8.31](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.31)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
