---
description: "Update all NuGet dependencies of one marcschier repo (source-only) and open a PR"
on:
  workflow_dispatch:
    inputs:
      repo:
        description: "Target repository under marcschier (e.g. dtls, crdt)"
        required: true
        type: string
engine: copilot
permissions:
  contents: read
network:
  allowed:
    - defaults
    - dotnet
tools:
  edit:
  bash: ["dotnet:*", "git:*", "ls", "cat", "grep", "head", "tail", "find", "pwd", "echo", "sed"]
  github:
    toolsets: [repos]
checkout:
  - repository: "marcschier/${{ github.event.inputs.repo }}"
    current: true
    fetch-depth: 0
    github-token: ${{ secrets.NUGET_UPDATE_TOKEN }}
steps:
  - name: Install .NET SDKs
    uses: actions/setup-dotnet@v4
    with:
      dotnet-version: |
        8.0.x
        9.0.x
        10.0.x
safe-outputs:
  create-pull-request:
    target-repo: "marcschier/${{ github.event.inputs.repo }}"
    github-token: ${{ secrets.NUGET_UPDATE_TOKEN }}
    base-branch: main
    draft: false
    labels: [dependencies, automation]
    title-prefix: "[nuget-update] "
    if-no-changes: ignore
  create-issue:
    target-repo: "marcschier/${{ github.event.inputs.repo }}"
    github-token: ${{ secrets.NUGET_UPDATE_TOKEN }}
    title-prefix: "[nuget-update] "
    labels: [automation]
    max: 1
    expires: false
---

# Update NuGet dependencies for a marcschier repository

You are updating the NuGet dependencies of the repository **`marcschier/${{ github.event.inputs.repo }}`**, which is already checked out in the current working directory. The .NET 8/9/10 SDKs are installed.

## Goal

Bring **every** NuGet dependency of this repository up to its **latest stable** version (including **major** upgrades), make only the **source-code** changes required to keep it building and its tests passing, and open a single pull request. The repository's own CI is the authority on correctness — your job is to produce a plausible, green-in-CI change.

## Steps

1. Run `dotnet restore` on the solution (`*.slnx` or `*.sln`), then `dotnet list <solution> package --outdated --format json` to find outdated packages.
2. If **nothing** is outdated, stop and make **no** pull request and **no** issue. Report "no updates".
3. Otherwise raise each outdated package to its latest **stable** version. Versions are managed centrally in `Directory.Packages.props` (Central Package Management) — edit the `<PackageVersion .../>` entries there (or the `.csproj` `<PackageReference Version="..."/>` where a repo pins locally). Update **all** outdated packages, including those used only by test/benchmark/sample projects.
4. Run `dotnet build <solution> -c Release`. Fix any breakages caused by the upgrades by editing **production source only** (files under `src/`). Prefer the smallest correct change that adapts to the new APIs.
5. Run `dotnet format <solution> --verify-no-changes` and fix formatting; keep lines within the repo's length limit (see `eng/` if present).
6. Run `dotnet test <solution> -c Release` where feasible. Some suites need external services (brokers, native libraries) that are not available here — that is fine; the repository's CI will run the full matrix on your PR.

## Hard rules

- **Never** modify anything under `tests/`, any `*.Tests*` project, `.github/`, `eng/`, `version.json`, `*.sln`/`*.slnx`, or coverage/lint configuration. These are protected.
- If the only way to make the build or tests pass is to change tests or CI, **do not** do it. Instead, open **one issue** (via the create-issue safe output) titled after the repo that explains which dependency update requires a test/CI change and why, and do **not** open a pull request.
- Do **not** bump `version.json` or create tags — releasing is handled separately by the conductor.
- Keep the change limited to dependency versions plus the minimal source fixes they require.

## Output

- On success: open **one** pull request (create-pull-request safe output) against `main` titled e.g. `[nuget-update] update NuGet dependencies`, with a body that lists each package bumped (old → new) and summarizes any source changes made.
- If blocked by the test/CI constraint: open the single explanatory issue instead.
