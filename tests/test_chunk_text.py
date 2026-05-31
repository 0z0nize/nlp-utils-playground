"""Smoke test for chunk_text."""

from utils import chunk_text  # noqa: F401


def test_import():
    assert chunk_text is not None
