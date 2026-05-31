"""Smoke test for strip_punct."""

from utils import strip_punct  # noqa: F401


def test_import():
    assert strip_punct is not None
