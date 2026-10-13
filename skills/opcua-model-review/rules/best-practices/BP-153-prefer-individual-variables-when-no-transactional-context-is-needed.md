---
id: "BP-153"
title: "Prefer individual Variables when no transactional context is needed"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.5.7", "7.5.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.7", "https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.2"]
---

# BP-153 - Prefer individual Variables when no transactional context is needed

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If no transactional context is needed, it is recommended to model structured data as individual Variables (clause 7.5.2's approach): the structure is directly visible in the AddressSpace, generic Clients can access it without custom-DataType knowledge, and individual parts can be referenced/annotated/written independently. Trade-off: no atomic read/write context and no single consistent timestamp across the parts.

## Applicability

Structured-data modelling decisions with no atomicity requirement.

## Exceptions and evidence limits

See BP-154 for when atomicity/interpretation constraints favor a structured-DataType approach instead.

## Audit

**NodeSet XML:** Not independently mechanical (a design-time choice); a tool can at best confirm that a modelled-as-individual-Variables substructure does not also claim/require atomic multi-Variable consistency in its documentation.

**Document:** Review rationale for the chosen granularity approach.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.5.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.7)
- [OPC 11030 v1.03.03, clause 7.5.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
