---
id: "BP-065"
title: "Do not change a released Method's signature"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.11"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.11"]
---

# BP-065 - Do not change a released Method's signature

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to change the signature of a released Method. The document is explicit that even adding a new *optional* Argument to an existing Method counts as a signature change and is therefore also disallowed.

## Applicability

Method Nodes, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

None  -  remediation is BP-068 (define a new Method instead), not an in-place exception.

## Audit

**NodeSet XML:** Diff `InputArguments`/`OutputArguments` arrays across versions for a given Method; flag any change in argument count, order, name, DataType, ValueRank, or mandatory/optional status.

**Document:** Compare Method argument tables across specification versions.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MUST NOT

## Source

- [OPC 11030 v1.03.03, clause 3.2.11](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.11)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
