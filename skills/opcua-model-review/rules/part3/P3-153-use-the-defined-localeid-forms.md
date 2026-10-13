---
id: "P3-153"
title: "Use the defined LocaleId forms"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.4"]
---

# P3-153 - Use the defined LocaleId forms

## Rule

LocaleIds follow the specified language/region conventions and documented extensions; an empty or null LocaleId denotes an unknown locale.

## Audit

Check supplied locale values without assuming the general BCP 47 language accepts every OPC UA-specific form.

## Source

- [OPC 10000-3 v1.05.06, clause 8.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
