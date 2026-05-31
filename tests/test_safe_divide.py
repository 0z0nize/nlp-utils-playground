"""Smoke test for safe_divide."""

from utils import safe_divide  # noqa: F401


def test_import():
    assert safe_divide is not None
