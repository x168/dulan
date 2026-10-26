"""Validate PR declarations and linked Issue metadata using GitHub REST."""

import argparse
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


PR_HEADINGS = ("變更摘要", "驗證", "風險與後續工作")
ISSUE_HEADINGS = (
    "Goal", "Owned scope", "Blocker state", "Blocker evidence",
    "Acceptance check", "Non-goals and follow-ups",
)
DECLARATIONS = (
    "已人工檢閱 diff、空白與文件連結，確認變更屬於認領範圍。",
    "建置、測試、lint 與相關回歸重現均交由自架 CI；未在開發機執行。",
    "已確認沒有提交憑證、帳號、token 或機密資料。",
)
REFERENCE = re.compile(
    r"\b(Closes|Tracks|Close|Closed|Fix|Fixes|Fixed|Resolve|Resolves|Resolved)"
    r"\s+(?:([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+))?#([1-9][0-9]*)\b",
    re.IGNORECASE,
)


def visible(body):
    body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
    body = re.sub(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$", "", body, flags=re.MULTILINE | re.DOTALL)
    body = re.sub(r"`[^`\n]+`", "", body)
    return body


def sections(body, headings):
    matches = list(re.finditer(r"^## (.+?)\s*$", body, re.MULTILINE))
    if tuple(match[1] for match in matches) != headings:
        raise ValueError("Required level-two headings are missing, duplicated, or out of order.")
    return {
        match[1]: body[match.end():matches[index + 1].start() if index + 1 < len(matches) else len(body)].strip()
        for index, match in enumerate(matches)
    }


def linked_issues(body, repository):
    references = []
    for match in REFERENCE.finditer(visible(body)):
        keyword, target, number = match.groups()
        if target and target.lower() != repository.lower():
            raise ValueError("Issue references must target this repository.")
        references.append((int(number), keyword.lower() != "tracks"))
    if not references:
        raise ValueError("Add Closes #<issue> or Tracks #<issue>.")
    return sorted(set(references))


def validate_body(body, repository):
    if re.search(r"\\[nt]", body):
        raise ValueError("Replace shell-mangled newline or tab escapes with actual whitespace.")
    clean = visible(body)
    parts = sections(clean, PR_HEADINGS)
    for name in PR_HEADINGS:
        if not parts[name] or parts[name] in ("待填", "TODO", "TBD"):
            raise ValueError(f"Complete the {name} section.")
    for declaration in DECLARATIONS:
        checked = re.findall(r"^- \[[xX]\] " + re.escape(declaration) + r"\s*$", parts["驗證"], re.MULTILINE)
        if len(checked) != 1:
            raise ValueError("Confirm each canonical declaration exactly once, only when true.")
    return linked_issues(clean, repository)


def validate_issue(issue, closes):
    if issue.get("pull_request"):
        raise ValueError("A task reference must name an Issue, not a pull request.")
    if closes and issue.get("state") != "open":
        raise ValueError("A closing reference must name an open Issue. Use Tracks for closed work.")
    labels = [label["name"] for label in issue.get("labels", [])]
    if "agent-task" not in labels:
        return
    if not any(label.startswith("area:") for label in labels):
        raise ValueError("The agent Issue requires an area label.")
    if sum(label.startswith("type:") for label in labels) != 1:
        raise ValueError("The agent Issue requires exactly one type label.")
    if sum(label.startswith("priority:") for label in labels) != 1 or not any(
        label in {"priority:P0", "priority:P1", "priority:P2", "priority:P3"} for label in labels
    ):
        raise ValueError("The agent Issue requires exactly one valid priority label.")
    if not issue.get("milestone"):
        raise ValueError("The agent Issue requires a milestone.")
    body = issue.get("body") or ""
    if re.search(r"\\[nt]", body):
        raise ValueError("The Issue contains shell-mangled newline or tab escapes.")
    parts = sections(visible(body), ISSUE_HEADINGS)
    if not all(parts.values()):
        raise ValueError("Complete every Issue section.")
    if parts["Blocker state"] not in {"cleared", "partially cleared", "not cleared"}:
        raise ValueError("Use one canonical Blocker state, with evidence in its separate section.")


def api_get(path):
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("A read-only GitHub token is required for current Issue metadata.")
    request = Request("https://api.github.com/" + path, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--body-file", type=Path)
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY", "x168/dulan"))
    args = parser.parse_args()
    try:
        if args.repository != "x168/dulan":
            raise ValueError("This contract is configured for x168/dulan.")
        if args.body_file:
            body = args.body_file.read_text(encoding="utf-8")
        else:
            event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
            pr = event["pull_request"]
            number = int(event["number"])
            current = api_get(f"repos/{args.repository}/pulls/{number}")
            if current["state"] != "open" or current["head"]["sha"] != pr["head"]["sha"]:
                raise ValueError("The PR is closed or its head changed. Validate its current revision.")
            body = current.get("body") or ""
        for number, closes in validate_body(body, args.repository):
            issue = api_get(f"repos/{args.repository}/issues/{number}")
            try:
                validate_issue(issue, closes)
            except ValueError as error:
                raise ValueError(f"Issue #{number}: {error}") from error
        print("PR body and linked Issue metadata satisfy the contract.")
    except (ValueError, KeyError, OSError, HTTPError, URLError) as error:
        print(f"PR contract failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
