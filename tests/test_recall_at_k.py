"""Smoke test for recall_at_k."""

from utils import recall_at_k  # noqa: F401


def test_import():
    assert recall_at_k is not None
