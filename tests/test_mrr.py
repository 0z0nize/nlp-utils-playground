"""Smoke test for mrr."""

from utils import mrr  # noqa: F401


def test_import():
    assert mrr is not None
