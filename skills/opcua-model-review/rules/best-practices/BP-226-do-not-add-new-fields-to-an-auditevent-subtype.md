---
id: "BP-226"
title: "Do not add new fields to an AuditEvent Subtype"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["15"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/15"]
---

# BP-226 - Do not add new fields to an AuditEvent Subtype

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Subtype of a base AuditEvent type should not introduce additional fields, since Clients that generically process OPC UA AuditEvents are generally not equipped to handle such extensions, and the base AuditEvents already provide all relevant information (worked example: a dedicated field for one specific Method input argument is unnecessary, since that information is already available via the base `InputArguments` field).

## Applicability

Subtypes of base AuditEvent types.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For an AuditEvent Subtype, flag any declared Property/field beyond what its base AuditEvent type already defines.

**Document:** Review custom audit EventType definitions for added fields.

**Assessment:** Static-checkable.

**Source wording:** SHOULD NOT

## Source

- [OPC 11030 v1.03.03, clause 15](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/15)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
