---
id: "BP-182"
title: "Let the Server assign NodeIds for Client-created Nodes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.13"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.13"]
---

# BP-182 - Let the Server assign NodeIds for Client-created Nodes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When a Client creates Nodes (and thereby NodeIds) in a Server, it is recommended that the Client not dictate the NodeId itself, but instead let the Server define the NodeId and return it to the Client.

## Applicability

AddressSpace/Method design for Client-driven Node creation (cross-ref clause 8.4).

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not a NodeSet-structural property; relevant to the design of creation Methods' output Arguments (confirm a creation Method returns the assigned NodeId rather than requiring the Client to supply one as input).

**Document:** Review Method signatures for Node-creation Methods.

**Assessment:** Semantically reviewable (Method design); actual behavior is Runtime-only.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.13](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.13)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
