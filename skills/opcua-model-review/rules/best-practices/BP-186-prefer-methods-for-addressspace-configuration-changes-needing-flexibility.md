---
id: "BP-186"
title: "Prefer Methods for AddressSpace configuration changes needing flexibility"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["8.1", "8.4"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.1", "https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.4"]
---

# BP-186 - Prefer Methods for AddressSpace configuration changes needing flexibility

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Using Methods, with arguments carrying the full configuration detail needed (e.g., placement of a new Node, which optional components to include, options for removal), provides the highest flexibility and is therefore the recommended general approach for AddressSpace configuration changes.

## Applicability

AddressSpace configuration-change mechanism design.

## Exceptions and evidence limits

See BP-187-BP-190 for the specific patterns available.

## Audit

**NodeSet XML:** Confirm configuration-change capability is exposed via Methods rather than only NodeManagement Services or implicit Variable-count writes.

**Document:** Review the specification's configuration-change mechanism design.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 8.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.1)
- [OPC 11030 v1.03.03, clause 8.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
