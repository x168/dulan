"""Exercise malformed bodies, metadata gates, and document path boundaries."""

import copy
from pathlib import Path
import tempfile
import unittest

from check_documents import check_file
from validate_pr_contract import DECLARATIONS, validate_body, validate_issue


def body(reference="Closes #2"):
    declarations = "\n".join("- [x] " + text for text in DECLARATIONS)
    return (
        "## 變更摘要\n\n建立 PR 契約與文件驗證。\n\n" + reference
        + "\n\n## 驗證\n\n已人工審閱完整差異與連結。\n\n" + declarations
        + "\n\n## 風險與後續工作\n\n自架 runner 供應尚待確認；Issue 保持開啟。\n"
    )


def issue():
    return {
        "state": "open",
        "labels": [{"name": name} for name in ("agent-task", "area:infrastructure", "type:chore", "priority:P2")],
        "milestone": {"number": 1},
        "body": (
            "## Goal\n\nOne outcome.\n\n## Owned scope\n\nScripts and workflows.\n\n"
            "## Blocker state\n\npartially cleared\n\n## Blocker evidence\n\nRunner not provisioned.\n\n"
            "## Acceptance check\n\nSelf-hosted checks.\n\n## Non-goals and follow-ups\n\nNo deployment.\n"
        ),
    }


class ContractTests(unittest.TestCase):
    def test_canonical_closing_and_tracking_bodies(self):
        self.assertEqual(validate_body(body(), "x168/dulan"), [(2, True)])
        self.assertEqual(validate_body(body("Tracks #2"), "x168/dulan"), [(2, False)])

    def test_shell_mangled_body_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_body(body().replace("\n", chr(92) + "n"), "x168/dulan")

    def test_missing_duplicate_or_reordered_heading_is_rejected(self):
        for broken in (
            body().replace("## 驗證", "### 驗證"),
            body() + "\n## 變更摘要\nExtra section.\n",
            body().replace("## 驗證", "## 風險與後續工作", 1),
        ):
            with self.subTest(body=broken), self.assertRaises(ValueError):
                validate_body(broken, "x168/dulan")

    def test_hidden_reference_does_not_satisfy_contract(self):
        for reference in ("<!-- Closes #2 -->", "```text\nCloses #2\n```", "~~~text\nCloses #2\n~~~", "`Closes #2`"):
            with self.subTest(reference=reference), self.assertRaises(ValueError):
                validate_body(body(reference), "x168/dulan")

    def test_missing_unchecked_or_commented_declaration_is_rejected(self):
        for replacement in ("- [ ] ", "<!-- - [x] "):
            with self.subTest(replacement=replacement), self.assertRaises(ValueError):
                validate_body(body().replace("- [x] ", replacement, 1), "x168/dulan")

    def test_empty_summary_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_body(body().replace("建立 PR 契約與文件驗證。\n\nCloses #2", "<!-- TODO -->"), "x168/dulan")

    def test_cross_repository_reference_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_body(body("Closes x168/daan#2"), "x168/dulan")

    def test_all_referenced_tasks_are_returned(self):
        self.assertEqual(validate_body(body("Closes #2\nTracks #4"), "x168/dulan"), [(2, True), (4, False)])

    def test_valid_agent_issue(self):
        validate_issue(issue(), True)

    def test_missing_or_duplicate_classification_is_rejected(self):
        for name in ("area:infrastructure", "type:chore", "priority:P2"):
            candidate = issue()
            candidate["labels"] = [label for label in candidate["labels"] if label["name"] != name]
            with self.subTest(missing=name), self.assertRaises(ValueError):
                validate_issue(candidate, False)
        for extra in ("type:docs", "priority:P1", "priority:P9"):
            candidate = issue()
            candidate["labels"].append({"name": extra})
            with self.subTest(extra=extra), self.assertRaises(ValueError):
                validate_issue(candidate, False)

    def test_milestone_and_blocker_evidence_are_required(self):
        candidate = issue()
        candidate["milestone"] = None
        with self.assertRaises(ValueError):
            validate_issue(candidate, False)
        candidate = issue()
        candidate["body"] = candidate["body"].replace("partially cleared", "ready")
        with self.assertRaises(ValueError):
            validate_issue(candidate, False)

    def test_closed_issue_can_only_be_tracked(self):
        candidate = issue()
        candidate["state"] = "closed"
        validate_issue(candidate, False)
        with self.assertRaises(ValueError):
            validate_issue(candidate, True)

    def test_pull_request_cannot_be_used_as_task_issue(self):
        candidate = issue()
        candidate["pull_request"] = {"url": "https://api.github.com/repos/x168/dulan/pulls/5"}
        with self.assertRaises(ValueError):
            validate_issue(candidate, False)

    def test_malformed_issue_headings_and_escapes_are_rejected(self):
        for value in ("## Goal\nOnly one section.", issue()["body"].replace("\n", chr(92) + "n")):
            candidate = copy.deepcopy(issue())
            candidate["body"] = value
            with self.subTest(body=value), self.assertRaises(ValueError):
                validate_issue(candidate, False)


class DocumentTests(unittest.TestCase):
    def test_existing_relative_link_and_external_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "target.md").write_text("Target\n", encoding="utf-8")
            (root / "source.md").write_text("[Target](target.md) [Official](https://example.org/)\n", encoding="utf-8")
            self.assertEqual(check_file(root, "source.md"), [])

    def test_missing_and_escaped_links_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for target in ("missing.md", "../outside.md", "%2e%2e/outside.md"):
                (root / "source.md").write_text(f"[Target]({target})\n", encoding="utf-8")
                with self.subTest(target=target):
                    self.assertTrue(check_file(root, "source.md"))

    def test_forbidden_paths_and_line_endings_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "build-output").mkdir()
            (root / "build-output/file.md").write_text("File\n", encoding="utf-8")
            self.assertTrue(check_file(root, "build-output/file.md"))
            (root / "script.py").write_bytes(b"print('hello')\r\n")
            self.assertTrue(check_file(root, "script.py"))


if __name__ == "__main__":
    unittest.main()
