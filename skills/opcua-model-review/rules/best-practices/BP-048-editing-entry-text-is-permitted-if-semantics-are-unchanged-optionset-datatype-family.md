---
id: "BP-048"
title: "Editing entry text is permitted if semantics are unchanged (OptionSet DataType family)"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.8"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8"]
---

# BP-048 - Editing entry text is permitted if semantics are unchanged (OptionSet DataType family)

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is allowed to change the text of an entry if the semantic is not changed (e.g. typo fixes/wording improvements)  -  the same permission as BP-046, restated for the OptionSet-DataType family.

## Applicability

Same as BP-047.

## Exceptions and evidence limits

Bounded by "semantic not changed."

## Audit

**NodeSet XML:** Same as BP-046.

**Document:** Same as BP-046.

**Assessment:** Semantically reviewable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
