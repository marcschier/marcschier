---
id: "P3-163"
title: "Clear reserved EventNotifier bits"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.59"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "values"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.59"]
---

# P3-163 - Clear reserved EventNotifier bits

## Rule

EventNotifier uses only the defined subscribe/history bits; reserved bits are zero.

## Audit

Check Objects and Views, including effective XML default values.

## Source

- [OPC 10000-3 v1.05.06, clause 8.59](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.59)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
