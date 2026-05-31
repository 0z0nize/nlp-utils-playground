"""Smoke test for cosine_sim."""

from utils import cosine_sim  # noqa: F401


def test_import():
    assert cosine_sim is not None
