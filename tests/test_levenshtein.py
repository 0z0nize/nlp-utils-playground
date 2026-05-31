"""Smoke test for levenshtein."""

from utils import levenshtein  # noqa: F401


def test_import():
    assert levenshtein is not None
