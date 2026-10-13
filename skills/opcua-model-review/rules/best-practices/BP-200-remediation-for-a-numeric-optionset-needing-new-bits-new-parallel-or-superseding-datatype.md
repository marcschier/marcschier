---
id: "BP-200"
title: "Remediation for a numeric OptionSet needing new bits: new parallel or superseding DataType"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["11.2.5"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.5"]
---

# BP-200 - Remediation for a numeric OptionSet needing new bits: new parallel or superseding DataType

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

For OptionSets based on numeric DataTypes, adding new bits is not allowed (cross-ref clause 3.2.7/BP-045). The alternatives: create a new DataType containing both the old and new bits (which then needs to replace the old one everywhere, with migration implications), or create a new DataType with only the additional bits, deployed alongside (not replacing) the old one wherever needed.

## Applicability

Companion Specifications needing to extend an already-released numeric-DataType-based OptionSet.

## Exceptions and evidence limits

None stated beyond the two alternatives.

## Audit

**NodeSet XML:** Confirm the old OptionSet DataType is retained unchanged (cross-ref BP-076/BP-045) and the new bits live in a genuinely new/additional DataType.

**Document:** Review the specification's migration narrative.

**Assessment:** Static-checkable (retention of old type) / semantically reviewable (overall strategy).

**Source wording:** MUST NOT (direct addition) / MAY (remediation alternatives)

## Source

- [OPC 11030 v1.03.03, clause 11.2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
