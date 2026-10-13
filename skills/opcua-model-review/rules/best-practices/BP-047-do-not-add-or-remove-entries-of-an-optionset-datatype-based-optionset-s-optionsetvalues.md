---
id: "BP-047"
title: "Do not add or remove entries of an OptionSet-DataType-based OptionSet's OptionSetValues"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.8"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8"]
---

# BP-047 - Do not add or remove entries of an OptionSet-DataType-based OptionSet's OptionSetValues

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

For an OptionSet that is itself a subtype of the OptionSet DataType, it is not allowed to add or remove entries of the `OptionSetValues` Property.

## Applicability

OptionSet-DataType-based OptionSet DataTypes.

## Exceptions and evidence limits

See BP-050 (subtype may add bits without changing length).

## Audit

**NodeSet XML:** Same diff approach as BP-045, applied to this DataType family.

**Document:** Compare OptionSet bit-tables across versions.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST NOT

## Source notes

Rationale given: existing Subtypes may already rely on the bits as currently defined; adding entries could collide with a Subtype's own extensions.

## Source

- [OPC 11030 v1.03.03, clause 3.2.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
