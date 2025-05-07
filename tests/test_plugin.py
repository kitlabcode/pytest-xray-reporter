"""Tests for the pytest-xray-reporter plugin."""
import json
import pytest
from pathlib import Path
import sys


def test_success():
    """A test that should pass."""
    assert True


@pytest.mark.xfail(reason="This test is expected to fail")
def test_failure():
    """A test that should fail."""
    assert False, "This test is expected to fail"


@pytest.mark.skip(reason="This test is skipped")
def test_skipped():
    """A test that should be skipped."""
    assert True


def test_with_output(capsys):
    """A test that produces output."""
    print("This is stdout")
    print("This is stderr", file=sys.stderr)
    assert True 