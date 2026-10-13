---
id: "BP-039"
title: "Do not add fields to a released Structure DataType"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.5"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.5"]
---

# BP-039 - Do not add fields to a released Structure DataType

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to add fields to a Structured DataType once released under an existing NamespaceUri.

## Applicability

Structured DataType Nodes, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

None at this location (remediation path is in clause 11.2.4, BP-199).

## Audit

**NodeSet XML:** Diff two NodeSet versions' `StructureDefinition/Field` lists for a given DataType; flag additions.

**Document:** Compare successive specification revisions' structure-field tables.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MUST NOT

## Source notes

Source groups add/remove/rename/retype into one sentence; this extraction splits them (BP-039-BP-042) into independently testable assertions since each is a distinct diff condition. Rationale given: changing any of these would change the wire encoding, breaking built-in encode/decode knowledge.

## Source

- [OPC 11030 v1.03.03, clause 3.2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
