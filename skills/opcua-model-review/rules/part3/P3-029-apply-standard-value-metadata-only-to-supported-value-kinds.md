---
id: "P3-029"
title: "Apply standard value metadata only to supported value kinds"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2"]
---

# P3-029 - Apply standard value metadata only to supported value kinds

## Rule

Apply standard string, byte-string, array, engineering-unit, and currency Properties only to the value kinds specified for them. DataVariable-only Properties do not belong on Properties.

## Audit

Review each standard Property's applicability: numeric EngineeringUnits, numeric CurrencyUnit, string/LocalizedText limits, ByteString limits, and non-scalar array metadata.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
