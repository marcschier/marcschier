---
id: "BP-137"
title: "Use Optional when a provider may not support the functionality at all"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.7"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.7"]
---

# BP-137 - Use Optional when a provider may not support the functionality at all

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

From a Client perspective, mandatory functionality is desirable (guaranteed availability); from a Server perspective, mandatory functionality can be challenging if it cannot always be provided. As a compromise, it is recommended to use the Optional ModellingRule when the provider/Server may not support the functionality at all.

## Applicability

ObjectType/VariableType member design (choosing Optional vs Mandatory).

## Exceptions and evidence limits

See BP-138 for the writable-Variable counter-case.

## Audit

**NodeSet XML:** Not independently mechanical (reflects a design judgement about provider capability); a tool can only confirm the resulting ModellingRule is one of the valid values.

**Document:** Review rationale for Optional vs Mandatory choices.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.2.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.7)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
