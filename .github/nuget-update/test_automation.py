#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parent


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


conductor = load_module("nuget_update_conductor", "conductor.py")


class ConductorStateTests(unittest.TestCase):
    def test_completed_full_cycle_starts_fresh(self):
        state = {"status": "done", "repos": {"dtls": {"phase": "done"}}}

        actual = conductor.prepare_run_state(state, started_at="2026-08-26T00:00:00Z")

        self.assertEqual(
            actual,
            {
                "status": "running",
                "cycle_started_at": "2026-08-26T00:00:00Z",
                "repos": {},
            },
        )

    def test_running_full_cycle_resumes(self):
        state = {"status": "running", "repos": {"dtls": {"phase": "awaiting-pr"}}}

        actual = conductor.prepare_run_state(state)

        self.assertIs(actual, state)
        self.assertEqual(actual["repos"]["dtls"]["phase"], "awaiting-pr")

    def test_halted_cycle_is_not_cleared(self):
        state = {"status": "halted", "repos": {"dtls": {"phase": "failed"}}}

        actual = conductor.prepare_run_state(state)

        self.assertIs(actual, state)
        self.assertEqual(actual["status"], "halted")

    def test_scoped_run_rechecks_completed_target(self):
        state = {
            "status": "done",
            "repos": {
                "dtls": {"phase": "done"},
                "pgm": {"phase": "done"},
            },
        }

        actual = conductor.prepare_run_state(
            state, "dtls", started_at="2026-08-26T00:00:00Z"
        )

        self.assertNotIn("dtls", actual["repos"])
        self.assertEqual(actual["repos"]["pgm"]["phase"], "done")
        self.assertEqual(actual["scope"], "dtls")

    def test_scoped_run_cannot_interrupt_running_cycle(self):
        with self.assertRaisesRegex(ValueError, "another cascade is running"):
            conductor.prepare_run_state({"status": "running", "repos": {}}, "dtls")

    def test_running_scoped_cycle_resumes(self):
        state = {
            "status": "running",
            "scope": "dtls",
            "repos": {"dtls": {"phase": "awaiting-promotion"}},
        }

        actual = conductor.prepare_run_state(state, "dtls")

        self.assertIs(actual, state)
        self.assertEqual(actual["repos"]["dtls"]["phase"], "awaiting-promotion")

    def test_different_scoped_run_cannot_interrupt_running_scope(self):
        state = {
            "status": "running",
            "scope": "dtls",
            "repos": {"dtls": {"phase": "awaiting-promotion"}},
        }

        with self.assertRaisesRegex(ValueError, "another cascade is running"):
            conductor.prepare_run_state(state, "pgm")

    def test_repository_tag_workflow_is_used(self):
        runs = [
            {
                "databaseId": 42,
                "headBranch": "v0.12.1-alpha",
                "createdAt": "2026-08-26T01:00:00Z",
            }
        ]
        with patch.object(conductor, "gh_json", return_value=runs) as gh_json:
            run_id = conductor.latest_tag_run(
                "openusd-dotnet",
                "release.yml",
                "v0.12.1-alpha",
                "2026-08-26T00:00:00Z",
            )

        self.assertEqual(run_id, 42)
        self.assertIn("release.yml", gh_json.call_args.args)


class NuGetVersionTests(unittest.TestCase):
    class Response:
        def __init__(self, versions: list[str]):
            self.versions = versions

        def __enter__(self):
            return self

        def __exit__(self, *_):
            return None

        def read(self):
            return json.dumps({"versions": self.versions}).encode()

    def test_latest_stable_excludes_prereleases(self):
        versions = ["1.0.0", "1.1.0", "1.2.0-alpha"]
        with patch.object(
            conductor.urllib.request, "urlopen", return_value=self.Response(versions)
        ):
            actual = conductor.nuget_latest("Example")

        self.assertEqual(actual, "1.1.0")

    def test_latest_prerelease_stays_in_channel(self):
        versions = ["0.11.0-alpha", "0.12.0-beta", "0.12.0-alpha", "0.12.1-alpha.1"]
        with patch.object(
            conductor.urllib.request, "urlopen", return_value=self.Response(versions)
        ):
            actual = conductor.nuget_latest("Example", "alpha")

        self.assertEqual(actual, "0.12.1-alpha.1")


class VersionTests(unittest.TestCase):
    def run_next_patch(self, current: str, latest: str, prerelease: str = "") -> dict:
        with tempfile.TemporaryDirectory() as tmp:
            version_json = Path(tmp) / "version.json"
            version_json.write_text(json.dumps({"version": current}), encoding="utf-8")
            args = [
                sys.executable,
                str(HERE / "next-patch.py"),
                "--version-json",
                str(version_json),
                "--latest",
                latest,
                "--write",
            ]
            if prerelease:
                args += ["--prerelease", prerelease]
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            output = json.loads(result.stdout)
            output["written"] = json.loads(version_json.read_text(encoding="utf-8"))["version"]
            return output

    def test_stable_patch_is_unchanged(self):
        actual = self.run_next_patch("1.2.3", "1.2.5")

        self.assertEqual(actual["next"], "1.2.6")
        self.assertEqual(actual["tag"], "v1.2.6")
        self.assertEqual(actual["written"], "1.2.6")

    def test_alpha_patch_preserves_channel(self):
        actual = self.run_next_patch("0.12.0-alpha", "0.12.0-alpha", "alpha")

        self.assertEqual(actual["next"], "0.12.1-alpha")
        self.assertEqual(actual["tag"], "v0.12.1-alpha")
        self.assertEqual(actual["written"], "0.12.1-alpha")


class ConfigurationTests(unittest.TestCase):
    def test_conductor_installs_openusd_pinned_sdk(self):
        workflow = (HERE.parent / "workflows" / "nuget-update-conductor.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("10.0.301", workflow)

    def test_updater_allows_supported_central_package_manifests(self):
        workflow = (HERE.parent / "workflows" / "nuget-update-repo.md").read_text(
            encoding="utf-8"
        )

        self.assertIn('- "Directory.Packages.props"', workflow)
        self.assertIn('- "Directory.Build.props"', workflow)

    def test_readme_and_release_descriptors_match(self):
        result = subprocess.run(
            [sys.executable, str(HERE / "parse-readme.py")],
            check=True,
            capture_output=True,
            text=True,
        )
        parsed = json.loads(result.stdout)

        self.assertIn("openusd-dotnet", parsed["order"])
        self.assertEqual(len(parsed["order"]), 12)

    def test_repositories_with_dedicated_release_workflows_are_configured(self):
        _, config = conductor.load_config()

        self.assertEqual(
            config["repos"]["opc-classic"]["tag_workflow"], "release.yml"
        )
        self.assertEqual(config["repos"]["opc-classic"]["prerelease"], "alpha")
        self.assertEqual(
            config["repos"]["openusd-dotnet"]["tag_workflow"], "release.yml"
        )


if __name__ == "__main__":
    unittest.main()
