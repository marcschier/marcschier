# OPC specification style sign-off

Audit an entire OPC specification against its repository-local style rubric, resolve findings with the editor, then verify approved fixes in a newly rendered edition. The workflow requires the local rubric and a reproducible Publisher setup. Independent verification also requires a host that can provide a separate reader. The skill does not bundle the rubric or require another marketplace plugin.

## Install

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install opc-spec-style-signoff@marcschier
```

For a bare installation from a local checkout, copy the `opc-spec-style-signoff` directory, including `references`, into your Copilot user skills directory or the target repository's `.github/skills/` directory.

Invoke `/opc-spec-style-signoff` in a session for the target repository. For example:

- "Perform a read-only sign-off audit of Part 2. Use only the repository-local style rubric and use HTML and Word from the same frozen snapshot."
- "Address the accepted findings, ask me about each remaining policy choice one at a time, then have an independent reader verify the fixes."

The result is one verdict with the exact edition, rule coverage, prior finding dispositions, approved exceptions and any remaining blockers. The skill does not authorize posting, publishing or changing source during a read-only review.
