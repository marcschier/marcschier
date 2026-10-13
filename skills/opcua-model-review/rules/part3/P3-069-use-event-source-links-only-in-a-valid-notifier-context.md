---
id: "P3-069"
title: "Use event-source links only in a valid notifier context"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.5.1", "7.17"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.17"]
---

# P3-069 - Use event-source links only in a valid notifier context

## Rule

HasEventSource sources are subscribing Objects/Views, or ObjectTypes in the permitted InstanceDeclaration context. The HasEventSource-subtype graph is acyclic.

## Audit

Check SubscribeToEvents where applicable and review the ObjectType context. Missing explicit links do not mean a Server cannot generate Events.

## Source

- [OPC 10000-3 v1.05.06, clause 5.5.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1)
- [OPC 10000-3 v1.05.06, clause 7.17](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.17)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
