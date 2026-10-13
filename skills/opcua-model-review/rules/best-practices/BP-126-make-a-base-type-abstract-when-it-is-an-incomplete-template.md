---
id: "BP-126"
title: "Make a base type abstract when it is an incomplete template"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.3"]
strength: "INFORMATIVE"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.3"]
---

# BP-126 - Make a base type abstract when it is an incomplete template

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Favor an abstract base type when it is a template containing the child types' common elements but is not "whole" in itself and should never be instantiated directly (worked example: a "parent" concept, which in reality is always either a mother or a father).

## Applicability

New type-hierarchy design (IsAbstract decision).

## Exceptions and evidence limits

N/A (one of two paired heuristics with BP-127).

## Audit

**NodeSet XML:** Not mechanically checkable (reflects a domain-semantic judgement); a tool can only confirm the resulting `IsAbstract` flag is internally consistent with whether the type has ever been instantiated.

**Document:** Review design rationale for the abstract/concrete choice.

**Assessment:** Semantically reviewable.

**Source wording:** Informative design heuristic (no shall/should verb; presented as a "design decision in favour of")

**Context guard:** Informative framing does not independently establish a conformance violation.

## Source

- [OPC 11030 v1.03.03, clause 7.2.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
