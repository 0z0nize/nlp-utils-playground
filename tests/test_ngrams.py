"""Smoke test for ngrams."""

from utils import ngrams  # noqa: F401


def test_import():
    assert ngrams is not None
