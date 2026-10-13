---
id: "BP-046"
title: "Editing OptionSetValues entry text is permitted if semantics are unchanged"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.7"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.7"]
---

# BP-046 - Editing OptionSetValues entry text is permitted if semantics are unchanged

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is allowed to change the text of an `OptionSetValues` entry if the semantic is not changed (e.g., fixing typos or improving wording).

## Applicability

Same as BP-045.

## Exceptions and evidence limits

Bounded by "semantic not changed"  -  a wording change that alters meaning is not covered by this permission (and would fall back under BP-045's spirit, though not literally restated there).

## Audit

**NodeSet XML:** Text-only diffs on entry display names/descriptions are expected to be non-violations; cannot mechanically confirm "semantics unchanged"  -  that is a human judgement.

**Document:** Review the nature of wording changes between versions.

**Assessment:** Semantically reviewable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.7)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
