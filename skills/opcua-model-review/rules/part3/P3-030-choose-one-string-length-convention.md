---
id: "P3-030"
title: "Choose one string length convention"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.4"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "values"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4"]
---

# P3-030 - Choose one string length convention

## Rule

A DataVariable must not provide both standard MaxStringLength and MaxCharacters.

## Audit

Compare standard namespace-qualified Property names, not coincidental vendor-defined names.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
