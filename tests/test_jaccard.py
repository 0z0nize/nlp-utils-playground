"""Smoke test for jaccard."""

from utils import jaccard  # noqa: F401


def test_import():
    assert jaccard is not None
