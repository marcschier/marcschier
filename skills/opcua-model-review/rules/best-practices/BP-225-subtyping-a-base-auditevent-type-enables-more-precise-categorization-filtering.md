---
id: "BP-225"
title: "Subtyping a base AuditEvent type enables more precise categorization/filtering"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["15"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/15"]
---

# BP-225 - Subtyping a base AuditEvent type enables more precise categorization/filtering

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Creating a Subtype of a base AuditEvent type (e.g. of `AuditUpdateMethodEventType`) allows Events to be categorized more precisely and enables simpler Client-side filtering.

## Applicability

AddressSpace design needing precise audit-event categorization.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Confirm any custom audit EventType is a Subtype of an appropriate base AuditEvent type.

**Document:** Review the custom audit EventType's supertype.

**Assessment:** Static-checkable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 15](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/15)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
