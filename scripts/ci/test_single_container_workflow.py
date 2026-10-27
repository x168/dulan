"""Keep document checks inside the shared, socket-free job environment."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]


class SingleContainerWorkflowTests(unittest.TestCase):
    def test_document_job_selects_the_shared_utility_scene(self):
        source = (ROOT / ".github/workflows/pr-validation.yml").read_text(encoding="utf-8")
        labels = source.split("    runs-on:\n", 1)[1].split("    timeout-minutes:", 1)[0]
        self.assertEqual(re.findall(r"(?m)^      - (.+)$", labels), [
            "self-hosted", "home-linux", "ci-family-utility", "ci-scene-dulan-docs",
            "slot-${{ github.run_id }}-${{ github.run_attempt }}-contract-documents",
        ])
        first = source.split("    steps:\n", 1)[1].split("      - name:")[1]
        self.assertIn("home-ci-environment check --scene dulan-docs", first)
        self.assertNotIn("/.dockerenv", source)
        self.assertNotRegex(source, r"(?m)^\s+(?:container|services):")
        self.assertNotRegex(source, r"\b(?:docker|podman|nerdctl)\s+(?:run|create|exec)\b")


if __name__ == "__main__":
    unittest.main()
