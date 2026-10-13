---
id: "P3-173"
title: "Use valid CurrencyUnitType metadata"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2", "8.61"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.61"]
---

# P3-173 - Use valid CurrencyUnitType metadata

## Rule

Currency metadata follows ISO 4217, uses -1 for unknown numeric code/exponent, preserves three-digit numeric-code presentation, and does not support non-decimal currencies.

## Audit

Review the Structured value and currency meaning; do not infer a decimal separator from the development machine's culture.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 8.61](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.61)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
