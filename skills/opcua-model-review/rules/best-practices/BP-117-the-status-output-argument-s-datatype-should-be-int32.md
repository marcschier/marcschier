---
id: "BP-117"
title: "The status output argument's DataType should be Int32"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["5.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.1"]
---

# BP-117 - The status output argument's DataType should be Int32

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The DataType of the application-specific status output argument should be an Integer, preferably Int32. The Information Model may document the meaning of the values in the Method's metadata.

## Applicability

The trailing status Argument described in BP-116.

## Exceptions and evidence limits

"Preferably Int32" leaves room for another Integer subtype, but Int32 is the stated preference.

## Audit

**NodeSet XML:** Confirm the Argument's `DataType` is Int32 (ns=0;i=6) or another Integer DataType.

**Document:** Review Method Argument tables for the DataType used.

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 5.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
