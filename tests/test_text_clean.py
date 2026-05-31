"""Smoke test for text_clean."""

from utils import text_clean  # noqa: F401


def test_import():
    assert text_clean is not None
