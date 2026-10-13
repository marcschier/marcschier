---
id: "BP-177"
title: "Avoid a generic \"Other\" enumeration value as an extensibility escape hatch"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.12.2"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.12.2"]
---

# BP-177 - Avoid a generic "Other" enumeration value as an extensibility escape hatch

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A special `Other` enumeration value can be defined to signal "none of the regular values apply," but this approach is not recommended because it gives no indication of what the actual value should be.

## Applicability

Enumeration DataType design anticipating extensibility needs.

## Exceptions and evidence limits

None stated; this is discouragement, not prohibition.

## Audit

**NodeSet XML:** Flag Enumeration DataTypes containing a generic catch-all value (e.g., named "Other"/"Unknown"/"Unspecified" with no further structure) as a candidate for reconsideration.

**Document:** Review enumeration value tables for this pattern.

**Assessment:** Static-checkable (pattern detection) / semantically reviewable (whether it's truly this anti-pattern).

**Source wording:** SHOULD NOT (explicitly "not recommended," not an absolute prohibition)

## Source

- [OPC 11030 v1.03.03, clause 7.12.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.12.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
