#!/usr/bin/env python3
"""Derive the ordered repo list from README.md (the source of truth).

README.md lists every project (as `### ...](https://github.com/marcschier/<repo>)` headings)
and its cross-repo dependencies (in the "Repo dependencies" table). This script extracts that
graph and emits a leaf-to-top topological order (dependencies before dependents), with an
alphabetical tie-break inside each dependency wave, so the release pipeline processes a repo
only after everything it depends on has already been released.

Usage:
    parse-readme.py [--readme PATH] [--repos-yml PATH] [--format json|order]

Output (json, default): {"order": [...], "depends": {repo: [deps...]}}
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_README = os.path.normpath(os.path.join(HERE, "..", "..", "README.md"))
DEFAULT_REPOS_YML = os.path.join(HERE, "repos.yml")

REPO_LINK_RE = re.compile(r"github\.com/marcschier/([A-Za-z0-9._-]+)")
BOLD_RE = re.compile(r"\*\*([A-Za-z0-9._-]+)\*\*")


def extract_repos(text: str) -> list[str]:
    """All repos referenced by a `### [name](.../marcschier/name)` heading, in file order."""
    repos: list[str] = []
    for line in text.splitlines():
        if line.startswith("###"):
            m = REPO_LINK_RE.search(line)
            if m and m.group(1) not in repos:
                repos.append(m.group(1))
    return repos


def extract_edges(text: str, repos: set[str]) -> dict[str, set[str]]:
    """Parse the dependency table: `| **repo** | dep, dep | ... |` -> depends[repo] = {deps}."""
    depends: dict[str, set[str]] = {r: set() for r in repos}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) < 2:
            continue
        col1, col2 = cells[0], cells[1]
        # Source repos = bolded names in column 1 that are known repos.
        sources = [n for n in BOLD_RE.findall(col1) if n in repos]
        if not sources:
            continue  # header / separator / prose row
        # Standalone rows use "—" (or empty) in column 2 -> no dependencies.
        if not col2 or col2 in {"—", "-", "–"} or "standalone" in col2.lower():
            continue
        deps = {n for n in re.split(r"[,\s]+", col2) if n in repos}
        for s in sources:
            depends[s] |= (deps - {s})
    return depends


def topo_order(depends: dict[str, set[str]]) -> list[str]:
    """Kahn's algorithm, dependencies first, alphabetical tie-break within each wave."""
    emitted: set[str] = set()
    remaining = set(depends)
    order: list[str] = []
    while remaining:
        ready = sorted(r for r in remaining if depends[r] <= emitted)
        if not ready:
            raise SystemExit(f"ERROR: dependency cycle among {sorted(remaining)}")
        for r in ready:
            order.append(r)
            emitted.add(r)
            remaining.discard(r)
    return order


def load_repos_yml_names(path: str) -> set[str]:
    """Best-effort read of the top-level repo keys under `repos:` without a yaml dependency."""
    names: set[str] = set()
    if not os.path.exists(path):
        return names
    in_repos = False
    for raw in open(path, encoding="utf-8"):
        if re.match(r"^repos:\s*$", raw):
            in_repos = True
            continue
        if in_repos:
            if re.match(r"^\S", raw):  # dedented back to a top-level key
                break
            m = re.match(r"^  ([A-Za-z0-9._-]+):\s*$", raw)
            if m:
                names.add(m.group(1))
    return names


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", default=DEFAULT_README)
    ap.add_argument("--repos-yml", default=DEFAULT_REPOS_YML)
    ap.add_argument("--format", choices=["json", "order"], default="json")
    args = ap.parse_args()

    text = open(args.readme, encoding="utf-8").read()
    repos = extract_repos(text)
    if not repos:
        raise SystemExit("ERROR: no repositories found in README.md")
    depends = extract_edges(text, set(repos))
    order = topo_order(depends)

    described = load_repos_yml_names(args.repos_yml)
    if described:
        missing = [r for r in order if r not in described]
        if missing:
            raise SystemExit(
                f"ERROR: README repos missing from repos.yml: {missing}. "
                "Add a release descriptor or update README."
            )

    if args.format == "order":
        print("\n".join(order))
    else:
        print(json.dumps({"order": order, "depends": {r: sorted(d) for r, d in depends.items()}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
