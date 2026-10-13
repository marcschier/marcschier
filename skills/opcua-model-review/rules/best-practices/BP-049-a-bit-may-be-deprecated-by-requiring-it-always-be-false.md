---
id: "BP-049"
title: "A bit may be deprecated by requiring it always be false"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.8"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8"]
---

# BP-049 - A bit may be deprecated by requiring it always be false

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If a specification intends to deprecate a bit of an OptionSet-DataType-based OptionSet, it can require ("require"  -  i.e. state in spec text) that the corresponding `validBit` shall always be set to false, rather than removing the entry outright.

## Applicability

Same as BP-047.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** None purely structural (the requirement lives in specification text/conformance rules, not a NodeSet attribute by itself); a `IsDeprecated`-style marker, if used, could be checked (cross-ref clause 14).

**Document:** Review specification conformance text for a stated always-false requirement on the bit.

**Assessment:** Semantically reviewable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
