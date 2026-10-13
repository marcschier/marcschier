---
id: "BP-224"
title: "Use (or subtype) the appropriate base AuditEvent type for auditable actions"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["15"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/15"]
---

# BP-224 - Use (or subtype) the appropriate base AuditEvent type for auditable actions

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The base OPC UA specification defines various AuditEvents, each with event fields for particular operations (worked example: calling a Method may generate an `AuditUpdateMethodEventType` Event, which already includes fields like `InputArguments`). If an AuditEvent is needed  -  e.g., to record invocation of a specific Method  -  either the base AuditEvent type can be used directly, or a Subtype of it can be defined.

## Applicability

AddressSpace/Method design needing audit-trail support.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For documented auditable actions, confirm the corresponding base AuditEvent type (or a Subtype of it) is used/generated.

**Document:** Review specification text describing audit behavior.

**Assessment:** Semantically reviewable; actual event generation is Runtime-only.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 15](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/15)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
