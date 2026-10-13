---
id: "BP-109"
title: "Avoid breaking changes in new Companion Specification versions"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.3"]
---

# BP-109 - Avoid breaking changes in new Companion Specification versions

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is highly recommended that Companion Specifications avoid breaking changes in new versions.

## Applicability

Companion Specification versioning practice generally.

## Exceptions and evidence limits

None stated (general principle; specific strategies follow).

## Audit

**NodeSet XML:** N/A directly; operationalized via the specific BP-032-BP-108 diff checks.

**Document:** Review version history/release notes for stated breaking changes.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD ("highly recommended")

## Source

- [OPC 11030 v1.03.03, clause 3.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
