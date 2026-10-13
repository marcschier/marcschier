---
id: "BP-071"
title: "Avoid changing a released ReferenceType's usage restrictions"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.14"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.14"]
---

# BP-071 - Avoid changing a released ReferenceType's usage restrictions

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

ReferenceTypes typically restrict their usage by limiting which SourceNodes/TargetNodes are allowed (today specified only as prose, not machine-readable constraints). Changing those rules  -  whether to allow more or fewer cases  -  should be avoided.

## Applicability

ReferenceType usage-restriction prose, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

See BP-072  -  this is explicitly **not** an absolute prohibition.

## Audit

**NodeSet XML:** Not structurally checkable (restrictions are prose-only per this clause).

**Document:** Compare ReferenceType usage-restriction prose across specification versions.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD NOT

## Source notes

The source is explicit that changing these rules "is not forbidden"  -  see BP-072. This rule must not be escalated to MUST NOT; doing so would convert a discouraged practice into a false prohibition, which the task instructions specifically warn against.

## Source

- [OPC 11030 v1.03.03, clause 3.2.14](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.14)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
