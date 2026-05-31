"""Smoke test for precision_at_k."""

from utils import precision_at_k  # noqa: F401


def test_import():
    assert precision_at_k is not None
