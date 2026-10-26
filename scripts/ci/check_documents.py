"""Check tracked paths, text line endings, and relative Markdown links."""

import re
from pathlib import Path, PurePosixPath
import subprocess
import sys
from urllib.parse import unquote, urlsplit


def check_file(root, name):
    errors = []
    parts = PurePosixPath(name).parts
    if any(part.startswith("build") or part in {"runtime-data", ".vs"} for part in parts[:-1]) or name.endswith(".credential"):
        errors.append(f"{name}: forbidden tracked path")
    path = root / name
    if path.is_symlink():
        errors.append(f"{name}: review symlink before adding it to the source contract")
        return errors
    data = path.read_bytes()
    if path.suffix in {".py", ".sh", ".yml", ".yaml", ".json", ".md"} or data.startswith(b"#!"):
        if b"\r" in data:
            errors.append(f"{name}: use LF line endings")
        try:
            source = data.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"{name}: use UTF-8 text")
            return errors
        if path.suffix == ".md":
            source = re.sub(r"```.*?```", "", source, flags=re.DOTALL)
            source = re.sub(r"`[^`\n]+`", "", source)
            for target in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", source):
                target = target.strip().split(' "', 1)[0].strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                destination = (root / unquote(parsed.path).lstrip("/")) if parsed.path.startswith("/") else path.parent / unquote(parsed.path)
                if not destination.resolve().is_relative_to(root.resolve()) or not destination.exists():
                    errors.append(f"{name}: missing or out-of-repository link target {target}")
    return errors


def main():
    root = Path.cwd()
    names = subprocess.check_output(["git", "ls-files", "-z"]).decode("utf-8").split("\0")
    errors = [error for name in names if name for error in check_file(root, name)]
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print("Tracked paths, text line endings, and relative Markdown link targets passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
