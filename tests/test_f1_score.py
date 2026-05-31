"""Smoke test for f1_score."""

from utils import f1_score  # noqa: F401


def test_import():
    assert f1_score is not None
