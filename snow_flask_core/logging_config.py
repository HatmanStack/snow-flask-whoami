"""Logging configuration for snow-flask-whoami application."""
import json
import logging
import os
from typing import Any


class JSONFormatter(logging.Formatter):
    """Formatter that outputs JSON-structured logs."""

    def format(self, record: logging.LogRecord) -> str:
        log_data: dict[str, Any] = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
        }
        if record.exc_info:
            log_data['exception'] = self.formatException(record.exc_info)
        return json.dumps(log_data)


def setup_logging() -> None:
    """Configure application logging."""
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    if os.environ.get('LOG_FORMAT') == 'json':
        handler.setFormatter(JSONFormatter())
    else:
        handler.setFormatter(
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        )

    root.handlers = [handler]
