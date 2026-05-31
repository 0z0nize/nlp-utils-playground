"""Smoke test for write_jsonl."""

from utils import write_jsonl  # noqa: F401


def test_import():
    assert write_jsonl is not None
