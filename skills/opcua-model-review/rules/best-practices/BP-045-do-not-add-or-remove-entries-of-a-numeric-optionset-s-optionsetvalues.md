---
id: "BP-045"
title: "Do not add or remove entries of a numeric-OptionSet's OptionSetValues"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.7"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.7"]
---

# BP-045 - Do not add or remove entries of a numeric-OptionSet's OptionSetValues

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

For an OptionSet based on a numeric DataType, it is not allowed to add or remove entries of the `OptionSetValues` Property, since that would change the interpretation of the DataType's bits.

## Applicability

Numeric-DataType-based OptionSet DataTypes.

## Exceptions and evidence limits

None stated (remediation path is in clause 11.2.5, BP-200).

## Audit

**NodeSet XML:** Diff the `OptionSetValues` Property's EnumValueType array across versions; flag added/removed entries (by bit position).

**Document:** Compare OptionSet bit-table rows across versions.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST NOT

## Source

- [OPC 11030 v1.03.03, clause 3.2.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.7)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
