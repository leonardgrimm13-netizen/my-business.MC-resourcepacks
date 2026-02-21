from __future__ import annotations

import builtins
from modimg.pipeline import build_main_engines, run_engines


MISSING = {"nudenet", "opennsfw2", "open_nsfw2", "ultralytics", "pytesseract"}


def test_missing_optional_libs_are_skipped(monkeypatch) -> None:
    real_import = builtins.__import__

    def fake_import(name, globals=None, locals=None, fromlist=(), level=0):
        root = name.split(".", 1)[0]
        if root in MISSING:
            raise ModuleNotFoundError(f"No module named '{root}'")
        return real_import(name, globals, locals, fromlist, level)

    monkeypatch.setenv("OCR_ENABLE", "1")
    monkeypatch.setattr(builtins, "__import__", fake_import)

    engines = build_main_engines(no_apis=True)
    results = run_engines(path="dummy.png", frames=[], engines=engines)

    by_name = {r.name: r for r in results}

    assert by_name["OCR text"].status == "skipped"
    assert by_name["NudeNet"].status == "skipped"
    assert by_name["OpenNSFW2"].status == "skipped"
    assert by_name["YOLO-World weapons"].status == "skipped"

    for result in by_name.values():
        assert result.status != "error"
