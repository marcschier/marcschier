---
id: "P3-016"
title: "Explain a Node when providing Description"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.6"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.6"]
---

# P3-016 - Explain a Node when providing Description

## Rule

A supplied Description explains the Node's meaning using LocalizedText.

## Audit

Review descriptions for semantic content, not merely presence. Description is optional; its absence alone is not a Part 3 violation.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.6](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.6)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
