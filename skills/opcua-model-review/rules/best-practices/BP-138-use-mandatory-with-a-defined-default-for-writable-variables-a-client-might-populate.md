---
id: "BP-138"
title: "Use Mandatory with a defined default for writable Variables a Client might populate"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.7"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.7"]
---

# BP-138 - Use Mandatory with a defined default for writable Variables a Client might populate

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

For a writable Variable whose value may instead be supplied by the Client, it is recommended to use the Mandatory ModellingRule together with a defined default/"not provided" behavior  -  rather than Optional  -  specifically so the Client always has a Node to write into. The default-not-provided value may be a DataType's NULL value (OPC 10000-6) where available, or a specific sentinel like "-1" or an empty string.

## Applicability

Writable Variable design where Client-side population is anticipated.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For Variables documented as Client-writable configuration with a "not yet configured" state, confirm ModellingRule is Mandatory (not Optional) and that a default/sentinel value convention is documented.

**Document:** Review specification text for the documented default/sentinel convention.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.2.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.7)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
