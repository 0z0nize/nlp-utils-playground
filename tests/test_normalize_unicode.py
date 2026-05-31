"""Smoke test for normalize_unicode."""

from utils import normalize_unicode  # noqa: F401


def test_import():
    assert normalize_unicode is not None
