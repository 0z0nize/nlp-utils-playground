"""Smoke test for tfidf_simple."""

from utils import tfidf_simple  # noqa: F401


def test_import():
    assert tfidf_simple is not None
