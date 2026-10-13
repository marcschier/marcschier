---
id: "BP-151"
title: "Use Placeholder ModellingRules on a Method only when its signature cannot be standardized"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.4"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.4"]
---

# BP-151 - Use Placeholder ModellingRules on a Method only when its signature cannot be standardized

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Method on an ObjectType typically uses the Optional or Mandatory ModellingRule (propagating that optionality to instances). A Method may instead use `OptionalPlaceholder`/`MandatoryPlaceholder`, in which case the ObjectType does not fix the Method's input/output Arguments  -  only its name  -  and each instance may use an appropriate signature. This approach should only be used when the signature genuinely cannot be standardized.

## Applicability

Method definitions on an ObjectType.

## Exceptions and evidence limits

None stated beyond the "cannot be standardized" condition.

## Audit

**NodeSet XML:** For Methods using `OptionalPlaceholder`/`MandatoryPlaceholder`, review whether a fixed signature could in fact have been standardized instead (semantic judgement); flag Placeholder Methods with suspiciously uniform signatures across instances as a candidate for converting to a fixed-signature Optional/Mandatory Method.

**Document:** Review rationale for choosing a Placeholder Method.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
