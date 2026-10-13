---
id: "BP-031"
title: "Method Argument names use PascalCase"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.6"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.6"]
---

# BP-031 - Method Argument names use PascalCase

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Method Argument names should use PascalCase (examples: `JobOrder`, `Status`).

## Applicability

Method Argument names.

## Exceptions and evidence limits

As with BP-023, specification **prose** in some Companion Specifications legitimately uses lower camelCase for the same Arguments; only the UANodeSet encoding is expected to be PascalCase.

## Audit

**NodeSet XML:** Flag non-PascalCase `Argument/Name` values in the NodeSet.

**Document:** Do not flag lowerCamelCase argument names appearing only in prose tables.

**Assessment:** Static-checkable (XML); prose exception is semantically reviewable context.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
