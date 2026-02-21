from __future__ import annotations

import subprocess
import sys


def test_cli_help() -> None:
    proc = subprocess.run(
        [sys.executable, "moderate_image.py", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 0
    help_text = f"{proc.stdout}\n{proc.stderr}"
    assert "--no-apis" in help_text


def test_main_import_smoke() -> None:
    __import__("modimg.cli")
    __import__("modimg.pipeline")
