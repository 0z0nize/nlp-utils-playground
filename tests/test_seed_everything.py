"""Smoke test for seed_everything."""

from utils import seed_everything  # noqa: F401


def test_import():
    assert seed_everything is not None
