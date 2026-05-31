"""Smoke test for read_lines."""

from utils import read_lines  # noqa: F401


def test_import():
    assert read_lines is not None
