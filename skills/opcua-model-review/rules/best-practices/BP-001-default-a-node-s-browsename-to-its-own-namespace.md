---
id: "BP-001"
title: "Default a Node's BrowseName to its own Namespace"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.1"]
---

# BP-001 - Default a Node's BrowseName to its own Namespace

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Unless a BrowseName is deliberately defined in a different Namespace, or some specific handling applies, the Namespace component of a Node's BrowseName should match the Namespace of its NodeId (i.e., the Node's own defining Namespace).

## Applicability

Any Node's BrowseName (QualifiedName: NamespaceIndex + Name).

## Exceptions and evidence limits

Explicitly allowed to differ "unless the BrowseName is defined in some other Namespace or there is some specific handling for the BrowseName"  -  the source does not enumerate what "specific handling" means, so this is a recognized, open-ended exception rather than an exhaustive list.

## Audit

**NodeSet XML:** For each `UANode`, compare the namespace index encoded in its `NodeId` attribute against the namespace index encoded in its `BrowseName` attribute (resolve both via the NodeSet's `NamespaceUris` table); flag mismatches for review (not automatic failure, since legitimate exceptions exist).

**Document:** N/A (structural attribute, not prose).

**Assessment:** Static-checkable (flagging candidate mismatches), but final disposition of a flagged mismatch is semantically reviewable because of the open-ended exception clause.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
