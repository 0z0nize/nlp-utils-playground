"""Smoke test for dedupe_preserve."""

from utils import dedupe_preserve  # noqa: F401


def test_import():
    assert dedupe_preserve is not None
