# marc-writer

Write technical documents in Marc Schier's voice: state the point early, explain
the failure mechanism, and make the recommendation implementable.

The skill uses the supplied [Writing Style Guide](STYLE.md), including its
19 principles, document-type patterns, and acceptance questions. It then invokes
[Claudism Killer](../claudism-killer) for a final edit against that guide.
The cleanup preserves deliberate questions, causal arguments, technical density,
and useful qualifications.

## Install

Install both skills from the marketplace:

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install claudism-killer@marcschier
copilot plugin install marc-writer@marcschier
```

`claudism-killer` is an explicit dependency, not bundled or installed
automatically by `marc-writer`. Version 1.0.1 adds the clean-output composition
contract; update an older install with `copilot plugin update claudism-killer`.

Or register both skills from a local clone:

```powershell
copilot skill add .\skills\claudism-killer
copilot skill add .\skills\marc-writer
```

Use `/skills reload` to refresh a running session. Update installed plugin copies
with `copilot plugin update marc-writer`.

## Use

```text
Write an architecture proposal in Marc's style using these requirements.
Make the recommendation explicit and include failure and rollback behavior.

Rewrite docs\Federation.md as Marc. Preserve its requirements and citations.

Draft a strategy memo in Marc Schier's voice. Treat the investment as a proposal,
not an approved commitment.

Audit this specification against Marc's guide without editing it.
```

Drafts and rewrites return clean prose by default. Ask for an editorial report
to see findings and measured cleanup counts. Audits are read-only.

The skill does not invent experience, consensus, evidence, or design decisions
to imitate the voice. Missing information is surfaced rather than filled with
plausible claims. The guide's corpus attribution is supplied provenance, not
an independently verified corpus packaged with this plugin.
