"""Tests for the pytest-xray-reporter plugin."""

import sys
from datetime import datetime, timezone, timedelta

import pytest
from pytest_xray_reporter.plugin import to_isoformat


def test_datetime_formatting() -> None:
    """Test that to_isoformat produces Xray-compatible datetime format."""
    # Test with UTC timezone
    dt = datetime(2024, 1, 1, 12, 0, 0, 123456, tzinfo=timezone.utc)
    result = to_isoformat(dt)
    assert result == "2024-01-01T12:00:00+00:00"

    # Test with no timezone (should default to UTC)
    dt = datetime(2024, 1, 1, 12, 0, 0, 123456)
    result = to_isoformat(dt)
    assert result == "2024-01-01T12:00:00+00:00"

    # Test with non-UTC timezone
    dt = datetime(2024, 1, 1, 12, 0, 0, 123456, tzinfo=timezone(offset=timedelta(hours=1)))
    result = to_isoformat(dt)
    assert result == "2024-01-01T12:00:00+01:00"


def test_success() -> None:
    """A test that should pass."""
    assert True


@pytest.mark.xfail(reason="This test is expected to fail")
def test_failure() -> None:
    """A test that should fail."""
    raise AssertionError("This test is expected to fail")


@pytest.mark.skip(reason="This test is skipped")
def test_skipped() -> None:
    """A test that should be skipped."""
    assert True


def test_with_output(capsys: pytest.CaptureFixture[str]) -> None:
    """A test that produces output."""
    print("This is stdout")
    print("This is stderr", file=sys.stderr)
    assert True
