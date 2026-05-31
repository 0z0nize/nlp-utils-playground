"""Smoke test for batch_iter."""

from utils import batch_iter  # noqa: F401


def test_import():
    assert batch_iter is not None
