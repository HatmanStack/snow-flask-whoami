"""Tests for logging configuration."""

import json
import logging
import os
import sys
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).parent.parent))

from snow_flask_core.logging_config import JSONFormatter, setup_logging


def test_json_formatter_basic() -> None:
    """JSONFormatter produces valid JSON."""
    formatter = JSONFormatter()
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test.py",
        lineno=1,
        msg="Test message",
        args=(),
        exc_info=None,
    )
    output = formatter.format(record)
    parsed = json.loads(output)

    assert parsed["level"] == "INFO"
    assert parsed["logger"] == "test"
    assert parsed["message"] == "Test message"
    assert "timestamp" in parsed


def test_setup_logging_default() -> None:
    """Default logging uses text format."""
    with mock.patch.dict(os.environ, {}, clear=True):
        setup_logging()
        root = logging.getLogger()
        assert len(root.handlers) == 1
        assert not isinstance(root.handlers[0].formatter, JSONFormatter)


def test_setup_logging_json() -> None:
    """LOG_FORMAT=json uses JSON formatter."""
    with mock.patch.dict(os.environ, {"LOG_FORMAT": "json"}):
        setup_logging()
        root = logging.getLogger()
        assert len(root.handlers) == 1
        assert isinstance(root.handlers[0].formatter, JSONFormatter)
