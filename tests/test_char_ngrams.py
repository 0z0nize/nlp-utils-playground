"""Smoke test for char_ngrams."""

from utils import char_ngrams  # noqa: F401


def test_import():
    assert char_ngrams is not None
