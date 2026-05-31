"""Smoke test for zscore."""

from utils import zscore  # noqa: F401


def test_import():
    assert zscore is not None
