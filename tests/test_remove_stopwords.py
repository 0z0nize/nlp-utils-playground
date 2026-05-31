"""Smoke test for remove_stopwords."""

from utils import remove_stopwords  # noqa: F401


def test_import():
    assert remove_stopwords is not None
