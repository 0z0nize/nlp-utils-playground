"""Smoke test for entropy."""

from utils import entropy  # noqa: F401


def test_import():
    assert entropy is not None
