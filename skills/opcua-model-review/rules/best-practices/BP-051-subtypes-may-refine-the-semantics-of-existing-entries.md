---
id: "BP-051"
title: "Subtypes may refine the semantics of existing entries"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.8"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8"]
---

# BP-051 - Subtypes may refine the semantics of existing entries

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Subtypes of an OptionSet-DataType-based OptionSet may refine the semantic of existing entries. The document defers the mechanics of this to OPC 10000-3.

## Applicability

Same as BP-047.

## Exceptions and evidence limits

N/A.

## Audit

**NodeSet XML:** None defined here (mechanics are in Part 3, out of scope).

**Document:** None defined here.

**Assessment:** Semantically reviewable / impossible without dependencies (detail lives in Part 3).

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

This rule is recorded only because 11030 explicitly grants the permission at this location; the "how" is explicitly out of scope ("see OPC 10000-3") and not independently verified by this extraction.

## Source

- [OPC 11030 v1.03.03, clause 3.2.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
