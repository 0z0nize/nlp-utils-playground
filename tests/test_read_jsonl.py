"""Smoke test for read_jsonl."""

from utils import read_jsonl  # noqa: F401


def test_import():
    assert read_jsonl is not None
