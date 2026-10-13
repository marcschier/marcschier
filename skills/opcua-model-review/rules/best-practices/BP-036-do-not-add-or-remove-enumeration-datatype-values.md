---
id: "BP-036"
title: "Do not add or remove Enumeration DataType values"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.4"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.4"]
---

# BP-036 - Do not add or remove Enumeration DataType values

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to add or remove values of a released Enumeration DataType.

## Applicability

Enumeration DataType Nodes, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

See BP-037 (subtype with a value subset is permitted).

## Audit

**NodeSet XML:** Diff two NodeSet versions; flag any added/removed `EnumValueType` entry on a pre-existing Enumeration DataType.

**Document:** Compare successive specification revisions' enumeration tables.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MUST NOT

## Source notes

Rationale given: old Clients would not expect new values, and old Servers might still emit removed values that new Clients cannot interpret.

## Source

- [OPC 11030 v1.03.03, clause 3.2.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
