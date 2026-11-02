# Contextual wording evaluation

The detector tests extract the contextual regexes from `SKILL.md` and check
synthetic raw candidates, case handling, paragraph wrapping and overlap counts.
They do not implement an editor or prove a semantic judgment. Raw snippets may
include protected syntax to demonstrate why search counts are not prose counts.

Run from the repository root with Python's standard library:

```powershell
python -B -m unittest discover -s skills\claudism-killer\tests -v
```

For manual skill evaluation, present each `text` in [cases.json](cases.json) to
the skill with the stated author guide. Compare its disposition, revision and
reason with the fixture. Protect code and link destinations before measuring
editable prose. A rewrite passes only if it preserves actor, technical meaning
and evidence level; matching a preferred word is insufficient.

In particular, reject edits that turn an unverified declaration into proven
support, alter a quoted standards term, or change a stable identifier. Keep
unresolved cases unchanged and ask for the missing context. Evaluate the full
passage where the fixture's reason identifies a context requirement.
