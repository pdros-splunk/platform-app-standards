"""Run the actual reusable workflow's navigation validator against fixtures."""

import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

WORKFLOW = (
    Path(__file__).resolve().parents[1]
    / ".github/workflows/reusable-readiness-assessment.yml"
)
SOURCE = textwrap.dedent(
    WORKFLOW.read_text()
    .split("python - <<'PYCODE'\n", 1)[1]
    .split("          PYCODE", 1)[0]
)


class NavigationTest(unittest.TestCase):
    def validate(
        self, nav, help_view="", support_view="", packaged=("help", "support")
    ):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "default/data/ui/nav").mkdir(parents=True)
            (root / "default/data/ui/views").mkdir()
            (root / "default/data/ui/nav/default.xml").write_text(nav)
            for name in packaged:
                (root / f"default/data/ui/views/{name}.xml").write_text(
                    "<dashboard><label>Help</label></dashboard>"
                )
            return subprocess.run(
                [sys.executable, "-c", SOURCE],
                cwd=root,
                capture_output=True,
                check=False,
                env={
                    **os.environ,
                    "APP_ID": "fixture",
                    "PRIVATE_HELP_VIEW": help_view,
                    "PRIVATE_SUPPORT_VIEW": support_view,
                },
            ).returncode

    def test_public_links_remain_required_by_default(self):
        nav = '<nav><a href="https://splunk-platform-apps.github.io/fixture"/><a href="https://github.com/splunk-platform-apps/fixture/issues"/></nav>'
        self.assertEqual(self.validate(nav), 0)
        self.assertNotEqual(self.validate("<nav><!--" + nav + "--></nav>"), 0)

    def test_packaged_private_help_and_support_are_accepted(self):
        nav = '<nav><collection label="Help"><view name="help"/><view name="support"/></collection></nav>'
        self.assertEqual(self.validate(nav, "help", "support"), 0)
        self.assertNotEqual(
            self.validate(nav, "help", "support", packaged=("help",)), 0
        )
        self.assertNotEqual(self.validate(nav, "help", ""), 0)
        self.assertNotEqual(self.validate(nav, "help", "help"), 0)

    def test_private_views_must_appear_in_the_help_menu(self):
        self.assertNotEqual(
            self.validate(
                '<nav><view name="help"/><view name="support"/></nav>',
                "help",
                "support",
            ),
            0,
        )
        self.assertNotEqual(self.validate("<nav/>", "../help", "support"), 0)


if __name__ == "__main__":
    unittest.main()
