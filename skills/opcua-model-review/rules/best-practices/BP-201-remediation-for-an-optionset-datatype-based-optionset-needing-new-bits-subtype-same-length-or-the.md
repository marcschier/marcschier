---
id: "BP-201"
title: "Remediation for an OptionSet-DataType-based OptionSet needing new bits: Subtype (same length) or the numeric-style alternatives"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["11.2.5"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.5"]
---

# BP-201 - Remediation for an OptionSet-DataType-based OptionSet needing new bits: Subtype (same length) or the numeric-style alternatives

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

For OptionSets that are themselves subtypes of the OptionSet DataType, adding new bits directly is also not allowed (cross-ref clause 3.2.8/BP-047). However, Subtypes can be created supporting additional bits, as long as the overall defined length is unchanged (cross-ref clause 3.2.8/BP-050/BP-052). As an alternative, the same parallel/superseding-DataType strategies as the numeric case (BP-200) may be applied instead.

## Applicability

Companion Specifications needing to extend an already-released OptionSet-DataType-based OptionSet.

## Exceptions and evidence limits

None stated beyond the alternatives listed.

## Audit

**NodeSet XML:** Confirm any Subtype used for this purpose preserves the original defined length (cross-ref BP-052's check).

**Document:** Review the specification's migration narrative.

**Assessment:** Static-checkable (length preservation) / semantically reviewable (overall strategy).

**Source wording:** MUST NOT (direct addition) / MAY (Subtype or the BP-200-style alternatives)

## Source

- [OPC 11030 v1.03.03, clause 11.2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
