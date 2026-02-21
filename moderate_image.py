#!/usr/bin/env python3
"""Thin entrypoint wrapper. The implementation lives in the modimg package."""
from __future__ import annotations
from modimg.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
