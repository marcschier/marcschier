---
id: "BP-156"
title: "Use eventing when data creation is server-triggered or must carry incident-specific context"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.5.7", "7.5.6"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.7", "https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.6"]
---

# BP-156 - Use eventing when data creation is server-triggered or must carry incident-specific context

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The eventing approach (clause 7.5.6) should be used when the data's creation is triggered by the Server independent of any Client-defined sampling rate, or when contextual metadata (e.g., job ID, operator/user ID) must accompany the data precisely at the moment it is produced. The document again judges eventing not well suited to the IP-configuration running example, suggesting instead that "quality data created when something is produced" is a better fit; it also notes an EventType could itself be modelled using a structured DataType (potentially with sub-variables) to carry its data.

## Applicability

Structured-data modelling decisions where server-triggered timing or incident context matters.

## Exceptions and evidence limits

Read-only; does not support Client-initiated configuration changes (noted as a disadvantage).

## Audit

**NodeSet XML:** Not independently mechanical.

**Document:** Review rationale for choosing an eventing approach.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD (conditional recommendation)

## Source

- [OPC 11030 v1.03.03, clause 7.5.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.7)
- [OPC 11030 v1.03.03, clause 7.5.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
