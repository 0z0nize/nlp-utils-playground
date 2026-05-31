"""Smoke test for tokenize_words."""

from utils import tokenize_words  # noqa: F401


def test_import():
    assert tokenize_words is not None
