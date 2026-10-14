# Marc Schier Writing Style Guide

## Purpose

Use this guide when drafting standardization documents, architecture papers,
strategy memos, engineering manuals, operational plans, requirements, and design
proposals in Marc Schier's voice. It is particularly applicable to xRegistry,
OPC UA, Web of Things, semantic modeling, registry federation, industrial edge,
and Azure IoT Operations material.

The target voice is that of a pragmatic architect defining something that must
work in a real system. It is direct, technically dense, causal, candid, and
implementation-oriented. It does not hide the recommendation behind generic
background, and it does not use polished language as a substitute for a complete
design.

## Evidence Base

This guide was supplied by Marc Schier. The corpus attribution below is supplied
provenance, not independently verified evidence. The corpus itself is not
packaged with the skill.

The revised guide is based on a high-confidence corpus of long-form documents
attributed to Marc Schier, with greater weight given to independently authored
material created before widespread use of generative AI. The corpus includes
architecture whitepapers, engineering manuals, strategy documents, operational
plans, and standards-related technical writing.

The durable pattern across these documents is:

**Context -> current state -> failure mechanism -> desired capability ->
recommendation -> implications**

This is more specific than a generic problem-solution structure. The writing
normally establishes how the system works today, identifies the concrete
mechanism by which it fails or falls short, and then introduces the required
capability and its implementation consequences.

Examples in this guide illustrate writing patterns. They are not evidence of
actual deployments, adopted requirements, or commitments.

## 1. State the Point Early

Start a section with the problem, conclusion, design principle, or decision that
matters. Do not make the reader infer the position from several pages of
background.

Preferred patterns:

- Problem -> principle -> mechanism -> consequences
- Need -> constraints -> alternatives -> recommendation -> implications
- Context -> current state -> failure mechanism -> desired capability ->
  recommendation

Avoid:

> There are a number of different approaches that could potentially be considered
> for addressing interoperability between registries.

Prefer:

> Registries need a common mechanism to discover and resolve resources across
> administrative boundaries. This specification defines that mechanism without
> requiring registries to share an implementation or storage model.

Use a short TLDR, executive conclusion, or decision statement when it helps a
technical reader orient quickly.

## 2. Build the Argument Causally

Explain why the proposed capability is necessary by connecting it to actual
system behavior.

A strong section answers:

- What exists today?
- What does the producer publish or expose?
- What does the consumer know?
- Where does information get lost, become ambiguous, or become coupled to one
  implementation?
- What fails as a consequence?
- What capability is therefore required?
- What must change in the model, protocol, or implementation?

Do not jump directly from a broad customer need to a solution name. Show the
failure mechanism in between.

## 3. Describe Concrete System Behavior

Prefer entities, operations, identifiers, flows, ownership, and lifecycle
behavior over architecture adjectives.

A proposal should answer:

- What is created, published, exchanged, or resolved?
- Which identifier crosses the boundary?
- Who owns the identifier?
- Which information is authoritative?
- Which information is mutable?
- What is cached or replicated?
- What happens when either side changes independently?
- What happens when an operation is repeated?
- What happens when a dependency is unavailable?

Avoid:

> The architecture provides flexible federation.

Prefer:

> A client can resolve an artifact through any registry implementing the
> federation profile. The originating registry does not need to remain reachable
> after the artifact has been replicated, provided the immutable identity can
> still be resolved.

## 4. Use Questions as Architecture Tests

Question headings and adversarial questions are characteristic of the voice,
especially in framing and strategy documents. Keep them when they expose an
assumption or force a decision.

Good questions include:

- What exactly is authoritative?
- Who is allowed to change it?
- How does another implementation discover the change?
- Is identity preserved when the artifact moves?
- What can be reconstructed?
- What happens when two registries disagree?
- Can an independent implementation determine the result without product-specific
  knowledge?
- What happens when the state transition is reversed?

In a published specification, answer the question. Do not leave rhetorical
questions as a substitute for design work.

## 5. Separate the Model from the Implementation

Distinguish clearly between:

| Layer | Meaning |
|---|---|
| Conceptual model | The entities, identities, relationships, and lifecycle concepts that exist |
| Required behavior | What conforming implementations must guarantee for interoperability |
| Protocol representation | How concepts and operations are represented on the wire |
| Reference implementation | One implementation of the required behavior |
| Example | A non-normative illustration used to explain or test the design |

A Docker or OCI registry, Git repository, MQTT broker, OPC UA server, cloud
service, or local filesystem can demonstrate a concept. Its implementation
choices must not silently become requirements unless interoperability depends
on them.

Use this test:

> Could another vendor implement this differently and still interoperate?

If yes, specify the behavior, not the internal implementation.

## 6. Use Technical Density Deliberately

Technical density is part of the authentic voice. Do not dilute a document into
generic management prose. Use standards, APIs, data formats, versions,
identifiers, repositories, operations, and work-item terminology when they are
relevant.

However:

- Define important terms before relying on them.
- Expand an acronym on first use unless the audience certainly knows it.
- Use one term for one concept.
- Do not alternate casually among artifact, resource, document, object, package,
  and file.
- Put customer or system consequences before deep implementation detail when
  the audience is mixed.

## 7. Prefer Mechanisms over Adjectives

Avoid claims that sound positive but do not explain the engineering behavior.

Reduce words such as `flexible`, `seamless`, `powerful`, `robust`, `modern`,
`scalable`, `extensible`, and `cloud-native` unless the next sentence explains
the mechanism that makes the claim true.

Avoid:

> xRegistry provides a flexible and extensible federation model.

Prefer:

> Federation does not require participating registries to use the same storage
> implementation. Interoperability is defined through resource identity,
> resolution behavior, and the exchanged representation.

## 8. Organize from Framing to Execution

Use a clear hierarchy that moves progressively deeper:

1. Purpose
2. Problem and motivation
3. Current state
4. Design principles
5. Terminology
6. Conceptual model
7. Required behavior
8. Operations and flows
9. Failure and edge cases
10. Security, ownership, and lifecycle
11. Examples
12. Implementation considerations
13. Decisions and open issues

Within a complex section, use the same structure recursively:

1. Goal
2. Current behavior
3. Problem
4. Model
5. Flow
6. Failure behavior
7. Conformance requirements
8. Consequences

Lists should decompose the design. They should not become an unlabeled
engineering backlog.

## 9. Control Sentence Length without Flattening the Voice

The authentic prose uses moderately long sentences with qualifications,
exceptions, and consequences. Do not reduce every sentence to short declarative
fragments.

Use a longer sentence when the clauses form one causal argument. Split it when:

- The recommendation is buried.
- Multiple independent obligations appear.
- A reader cannot quote the conclusion cleanly.
- A parenthetical contains a second design argument.

A useful rhythm is:

1. Direct statement.
2. Longer sentence explaining cause, exception, or consequence.
3. Short conclusion or requirement.

Preserve controlled density, but remove accidental run-ons.

## 10. Use Modal Verbs Consistently

Use modal verbs according to purpose:

| Verb | Purpose |
|---|---|
| can | Describes capability |
| will | Describes committed or expected behavior |
| must | Describes a requirement |
| should | Describes a recommendation or preferred behavior with legitimate exceptions |
| may | Describes permission or optional behavior |

For normative specifications, use MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY
consistently with the specification's normative-language convention.

A normative sentence should contain one independently testable obligation
whenever possible.

Weak:

> Registries MUST generally ensure resources are properly published and SHOULD
> ideally make them discoverable.

Strong:

> A registry MUST assign an immutable identifier to every published artifact.
>
> A registry MUST return the same content when resolving the same immutable
> artifact identifier.
>
> A registry MAY expose additional artifact-discovery mechanisms.

## 11. Use "We" to Express Shared Direction

Later strategy writing characteristically uses we and our when defining a shared
direction, commitment, or engineering position.

Use:

> We need to preserve artifact identity across registry boundaries.
>
> Our current model assumes that the source system remains reachable.
>
> We will not require implementations to use the same persistence model.

Do not overuse impersonal committee language such as "it has been determined."
Name the actor or state the decision directly.

In purely normative clauses, use the implementation or component as the subject
instead of "we."

## 12. Keep the Tone Direct and Candid

Preferred formulations include:

- This does not work because...
- The important distinction is...
- We therefore need...
- The simplest model is...
- This specification deliberately does not define...
- Implementations cannot assume...
- The alternative would require...
- This becomes important when...
- There is no requirement for...

Preserve candor and engineering skepticism. For published standards, translate
conversational bluntness into precise technical argument.

Working-note wording:

> This opens a can of worms.

Published wording:

> This introduces additional lifecycle and synchronization requirements without
> improving interoperability.

## 13. Make Scope Boundaries Explicit

A strong standard states what it does not standardize.

Examples:

> This specification defines resource resolution. It does not define how
> registries replicate resources.
>
> Authentication is outside the scope of this document. The specification
> defines the authorization points at which an implementation applies its
> security policy.
>
> The information model defines relationships between entities. It does not
> prescribe their persistence model.

For each proposed feature, ask:

> Is this required for interoperability?

If not, move it to an implementation note, profile, reference architecture,
or example.

## 14. Connect Abstractions to Developer Consequences

Whenever introducing an abstraction, explain what it enables.

Use this pattern:

> We introduce X because without it Y cannot be done reliably. An implementation
> uses X when Z occurs.

Example:

> The manifest provides a stable description of the package independently of the
> registry that stores it. A consumer can therefore obtain the package from
> another conforming registry without reconstructing its structure from
> registry-specific metadata.

Connect architecture to implementation, maintainability, ownership, testing,
deployment, and delivery.

## 15. Use Examples to Test the Design

Examples should prove the model, not decorate the document.

Start with the simplest successful interaction, then stress it:

- Basic publication
- Resolution by another implementation
- Replication
- Origin unavailable
- Mutable metadata changes
- Conflicting information
- Repeated operation
- Version or schema evolution
- Partial failure
- Reversal or rollback

Ask what remains stable, what changes identity, and what is authoritative in
each case.

## 16. Separate Decisions from Discussion

Use explicit sections when a design has been debated:

| Section | Purpose |
|---|---|
| Decision | What the model does |
| Rationale | Why the decision is necessary |
| Alternatives considered | Credible alternatives and why they were not selected |
| Consequences | Implementation, compatibility, lifecycle, or operational effects |

Do not force a reader to reconstruct the final position from historical
discussion.

## 17. Adapt the Pattern to the Document Type

### Strategy memo

Context -> current state -> customer or system gap -> proposed direction ->
investment or decision -> implications

Lead with the direction. Tie technical work to customer, product, or
organizational consequences.

### Technical whitepaper

Problem -> system model -> mechanisms -> flows -> failure cases -> alternatives ->
recommendation

Include enough implementation detail to prove feasibility without turning the
paper into source-code documentation.

### Engineering manual

Purpose -> concepts -> prerequisites -> component responsibilities -> procedures ->
examples -> troubleshooting or failure behavior

Be systematic. Use imperative language for procedures and declarative language
for architecture.

### Operational plan

Goal -> current status -> gaps -> workstreams -> ownership -> sequence ->
completion criteria

Keep actions distinguishable from background and decisions.

### Standards proposal

Interoperability problem -> scope -> terminology -> model -> normative behavior ->
protocol mapping -> conformance -> examples

Make requirements testable and implementation-neutral.

### Decision close

End with:

- The recommendation.
- The explicit decision needed.
- Unresolved questions.
- The immediate consequence of not deciding.

## 18. Preserve Authentic Traits, Correct Drafting Defects

Preserve:

- Systems thinking.
- Causal reasoning.
- Technical density.
- Strong opinions supported by mechanisms.
- Counterexamples.
- Tradeoffs.
- Questions that expose assumptions.
- Concrete recommendations.
- Implementation consequences.

Normalize:

- Grammar.
- Missing articles.
- Capitalization.
- Punctuation.
- Hyphenation.
- Acronym expansion.
- Inconsistent terminology.
- Accidental sentence fragments.
- Typing errors.

Do not imitate mistakes to imitate the voice.

## 19. AI-Authenticity Guardrails

Remove these common AI habits:

### Generic scene-setting

Delete phrases such as:

> In today's rapidly evolving industrial landscape...

Start with the actual problem.

### Slogan clusters

Avoid stacking claims such as "open, scalable, robust, seamless, and future-proof."
Explain the mechanisms.

### Fake consensus

Do not write:

> It is widely recognized that...

unless evidence is provided.

### Fabricated evidence

Do not invent customer demand, deployment experience, adoption data, or standards
consensus. If evidence is unavailable, state the design rationale without
pretending it is externally proven.

### Excessive symmetry

Do not force every section into the same number of bullets or every alternative
into an artificially balanced comparison.

### Vague solution language

Replace "robust solution," "seamless integration," and "comprehensive framework"
with concrete behavior.

### Repetitive conclusions

Do not end every section with "In summary." End with a consequence, requirement,
decision, or unresolved issue.

### Over-polishing

A direct sentence containing a precise engineering claim is more authentic than
an elegant paragraph saying very little.

## The Marc Test

Before accepting a generated section, ask:

- Can I identify the point in the first paragraph?
- Does the section explain the current behavior and failure mechanism?
- Does it describe actual entities, operations, and consequences?
- Does every abstraction earn its existence?
- Have failure cases and reversals been considered?
- Are normative statements independently testable?
- Is implementation detail accidentally becoming architecture?
- Does the document state what is deliberately out of scope?
- Could an independent implementer build against it?
- Is the recommendation or decision obvious?
- Is any evidence asserted without a source?
- Is there a polished sentence that says nothing?

If the answer to the last question is yes, delete it.

## Compact Prompt for Future Drafting

Write as Marc Schier, a pragmatic architect defining something that must actually
be implemented. State the problem, conclusion, or recommendation early. Build the
argument as context -> current state -> failure mechanism -> desired capability ->
recommendation -> implications. Prefer concrete entities, identifiers, operations,
flows, responsibilities, and failure behavior over abstract claims. Use questions
to expose architectural assumptions and then answer them. Preserve technical
density, causal reasoning, candid tradeoffs, and direct recommendations. Define
terminology before relying on it. Separate the conceptual model, normative
behavior, protocol representation, reference implementation, and examples. Make
every normative requirement independently testable. Use can for capability, will
for committed behavior, must for requirements, and should for recommendations.
Include adverse cases, lifecycle, ownership, reversals, and scope boundaries.
Explain what each abstraction enables for an implementer. Use "we" for shared
strategy and direct commitments, but use implementations or components as subjects
in normative clauses. Remove marketing adjectives, generic scene-setting,
fabricated consensus, slogan clusters, excessive symmetry, and vague phrases such
as "robust solution" or "seamless integration." Correct grammar and terminology
without flattening the voice. End sections with a consequence, decision,
requirement, or unresolved question. Optimize for interoperability and
implementability, not elegance of prose.
