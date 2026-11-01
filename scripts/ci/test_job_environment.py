"""Exercise the actual admitted Linux document-job workspace in self-hosted CI."""
import json
import os
from pathlib import Path
import platform
import stat
import subprocess
import sys
import tempfile
import unittest
from contextlib import ExitStack


JOB_ROOT = Path("/workspace")


@unittest.skipUnless(sys.platform.startswith("linux"), "Shared Linux task contract")
class JobEnvironmentTests(unittest.TestCase):
    def test_actual_sdk_acknowledges_the_selected_scene_and_native_platform(self):
        expected = os.environ["DULAN_CI_EXPECTED_ARCH"]
        self.assertIn(expected, ("amd64", "arm64"))
        self.assertEqual(
            {"x86_64": "amd64", "aarch64": "arm64"}[platform.machine().lower()],
            expected,
        )
        acknowledgment = Path(os.environ["TMPDIR"]) / "dulan-docs-environment.json"
        self.assertFalse(acknowledgment.is_symlink())
        information = acknowledgment.stat()
        self.assertEqual(information.st_uid, os.geteuid())
        self.assertEqual(stat.S_IMODE(information.st_mode), 0o600)
        self.assertGreater(information.st_size, 0)
        self.assertLessEqual(information.st_size, 65536)
        result = json.loads(acknowledgment.read_text(encoding="utf-8"))
        self.assertIs(result["verified"], True)
        self.assertEqual(result["scene"], "dulan-docs")
        self.assertEqual(result["platform"], "linux/" + expected)
        self.assertRegex(result["shared_tools"]["catalog_sha256"], r"\A[0-9a-f]{64}\Z")
        self.assertGreater(len(result["shared_tools"]["layer_diff_ids"]), 0)

    def test_private_job_paths_support_an_isolated_child_roundtrip(self):
        self.assertEqual(os.environ["DAAN_CI_JOB_ROOT"], str(JOB_ROOT))
        self.assertEqual(Path(os.environ["HOME"]), JOB_ROOT / "home")
        self.assertEqual(Path(os.environ["TMPDIR"]), JOB_ROOT / "tmp")
        directories = [
            JOB_ROOT / "home",
            JOB_ROOT / "tmp",
            JOB_ROOT / "runner" / "_work",
            JOB_ROOT / "artifacts",
        ]
        for directory in [JOB_ROOT, *directories]:
            with self.subTest(directory=directory.name):
                self.assertTrue(directory.is_dir())
                self.assertFalse(directory.is_symlink())
                self.assertTrue(directory.resolve().is_relative_to(JOB_ROOT.resolve()))
        for directory in [JOB_ROOT, JOB_ROOT / "home", JOB_ROOT / "tmp"]:
            information = directory.stat()
            self.assertEqual(information.st_uid, os.geteuid())
            self.assertEqual(stat.S_IMODE(information.st_mode) & 0o077, 0)
        for name in ("RUNNER_TEMP", "GITHUB_WORKSPACE"):
            with self.subTest(environment=name):
                value = Path(os.environ[name])
                self.assertTrue(value.is_absolute())
                self.assertTrue(value.resolve().is_relative_to(directories[2].resolve()))

        # Parent modes can differ. Each new fixture must have its own private owner boundary.
        with ExitStack() as stack:
            private = [
                Path(stack.enter_context(tempfile.TemporaryDirectory(
                    prefix="dulan-job-contract-", dir=directory,
                )))
                for directory in directories
            ]
            for directory in private:
                self.assertEqual(directory.stat().st_uid, os.geteuid())
                self.assertEqual(stat.S_IMODE(directory.stat().st_mode), 0o700)
            child = """import json, os, pathlib, stat, sys
roots = [pathlib.Path(value) for value in sys.argv[1:]]
for root in roots:
    path = root / 'roundtrip.txt'
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, 'w', encoding='utf-8') as stream:
        stream.write('dulan-private-job-roundtrip\\n')
    assert path.read_text(encoding='utf-8') == 'dulan-private-job-roundtrip\\n'
    assert path.stat().st_uid == os.geteuid()
    assert stat.S_IMODE(path.stat().st_mode) == 0o600
print(json.dumps({'roundtrips': len(roots), 'isolated': bool(sys.flags.isolated),
                  'site_disabled': bool(sys.flags.no_site)}))
"""
            result = subprocess.run(
                [sys.executable, "-I", "-S", "-B", "-c", child, *map(str, private)],
                cwd=private[1], capture_output=True, text=True, timeout=15,
                check=False,
            )
            self.assertEqual(result.returncode, 0, "The isolated job child failed")
            self.assertLessEqual(len(result.stdout), 4096)
            self.assertEqual(json.loads(result.stdout), {
                "roundtrips": 4, "isolated": True, "site_disabled": True,
            })
            for directory in private:
                self.assertEqual(
                    (directory / "roundtrip.txt").read_text(encoding="utf-8"),
                    "dulan-private-job-roundtrip\n",
                )


if __name__ == "__main__":
    unittest.main()
