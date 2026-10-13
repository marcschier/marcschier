---
id: "BP-166"
title: "Use the least complex adequate DataType"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.9"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9"]
---

# BP-166 - Use the least complex adequate DataType

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Use the least complex DataType that does the job  -  worked examples: prefer integer over floating point when adequate; prefer a numeric-DataType-based OptionSet over an OptionSet-DataType-based OptionSet when adequate.

## Applicability

New DataType/field design decisions.

## Exceptions and evidence limits

Only when the simpler type is in fact adequate for the need.

## Audit

**NodeSet XML:** Flag floating-point fields holding values that are always integral by documented semantic, or OptionSet-DataType-based OptionSets with no documented need for the extra flexibility that family provides over a numeric OptionSet.

**Document:** Review DataType choice rationale.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
