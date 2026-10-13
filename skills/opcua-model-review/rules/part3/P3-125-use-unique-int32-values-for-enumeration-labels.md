---
id: "P3-125"
title: "Use unique Int32 values for Enumeration labels"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.39"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.39"]
---

# P3-125 - Use unique Int32 values for Enumeration labels

## Rule

An EnumValues array has unique integer values; when representing an Enumeration DataType those values fit Int32.

## Audit

Decode EnumValueType values and compare them numerically. Other uses of EnumValueType may legitimately use its wider Int64 domain.

## Source

- [OPC 10000-3 v1.05.06, clause 8.39](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.39)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
