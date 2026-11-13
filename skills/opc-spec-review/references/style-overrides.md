# Temporary specification-style safeguards

These preventive safeguards take precedence over conflicting instructions in
`opcua-spec-style`, including its examples. They do not attribute every
potential loss to that skill: publisher composition can independently omit
model facts. Apply them to review, proposals and authorized edits. They do not
authorize writes or technical changes.

The style skill's `rules.md` takes precedence over contradictory examples;
these safeguards take precedence over both. The specification's applicable
normative sources establish technical facts, not the style skill. The
repository's authoring contract and pinned Publisher own syntax and output
mechanics; neither authorizes loss of a requirement.

## Ownership and persistence

- Identify whole `BEGIN GENERATED MODEL REFERENCE` through `END GENERATED MODEL
  REFERENCE` regions as well as bound table cells. Do not edit them or move
  authored requirements into them. `table=keep` protects against compose, not
  an outer generator. Propose a generator-input change or a persistent authored
  home; do not casually change frozen NodeSet descriptions. In approved
  isolation, verify persistence through the repository's regeneration and
  determinism checks. Read-only reviews run no writing commands.
- Inventory all information before removal, not just shall/should/may counts.
  "Already in the NodeSet" is not sufficient: identify an accessible rendered
  specification text, table or exact applicable normative reference with
  equivalent meaning and scope. Preserve useful facts without forcing duplicate
  prose when a genuinely equivalent published home exists. A compose check or
  build does not prove semantic completeness.
- Inventory every definition and every term used in normative text, including
  newly introduced names, scope, first-use resolution and distinguishing
  properties of similar roles. Reconcile each definition and use; do not
  discard distinctions as rationale.
- Preserve prohibitions, no-state-change on error, absence semantics and
  operation or ordering limits when they express facts. B6 and B7 do not
  authorize blanket deletion. A shared requirement may have one canonical
  cross-cutting home with references; moving it into a single Node or Method
  must not narrow its scope.
- Preserve provisional identifier, registration and release-status disclosures
  in an appropriate persistent location. C5 is a modelling flag, not deletion
  authority.
- Before merging mapping tables, inventory every external member or key, row,
  field and value, encoding, omitted or not-mapped case; reconcile its retained
  treatment and scope.

## Contracts and publication

- Do not turn descriptive or illustrative statements into new `shall`
  requirements or mandatory status codes. Keep proposals separate from
  normative specification text until a technical decision is secured. Persist
  Dropped, Moved and Flags in authorized review artifacts, correlate affected
  CTT expectations, and do not treat a transient chat flag as approval.
- Before heading, table or layout changes, inventory repository-wide inbound
  references, including sibling specs and hard-coded clause numbers,
  manifests, includes, profiles, tests, validators and annexes. In read-only
  review report the impact; for approved edits update allowed dependencies or
  flag out-of-scope fixes. Use the actual repository baseline and compare
  after validation, not a fixed command assumed to work everywhere.
- Reconcile all table facts, including ReferenceType InverseName and Symmetric,
  Structure encoding references, field order, dimensions, ModellingRules and
  reserved-bit semantics. An equivalent published home can suffice; do not
  blindly reinstate redundant rows. Publisher omissions are dependencies, not
  authority to delete content or edit tooling outside scope.
- For D8 table consolidation, reconcile the repository's AUTHORING contract,
  validators and generator ownership. Report conflicts and seek a decision
  rather than rewriting contracts or dropping tables. Assess consistency
  within the agreed release set; do not initiate an all-repository migration.
- Use the repository-approved pinned toolchain and validate restore and
  validator compatibility. Do not impose the version floor in upstream
  examples, silently substitute a version or change pins.

## Conflicting examples and retirement

Examples illustrate rather than override rules or these safeguards. In
particular, do not promote descriptive text to `shall`, omit a required child
name and kind, or prefer code formatting over the rules' semantic emphasis
because an example does so. Do not adopt an example's editorial ordering as
policy. Treat placeholder anchors as literal syntax in code or fenced samples,
not actionable broken links.

Each safeguard is temporary and independently removable only after inspecting
an identified corrected upstream revision and verifying the corresponding
synthetic regression behavior. Record the revision and evidence for each
removal. Until then keep it, even if another safeguard has been retired.
