"""Smoke test for confusion_matrix."""

from utils import confusion_matrix  # noqa: F401


def test_import():
    assert confusion_matrix is not None
