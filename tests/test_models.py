"""Tests for type definitions."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from snow_flask_core.models import ChartData, ChartDataPoint


def test_chart_data_point_structure() -> None:
    """ChartDataPoint has correct structure."""
    point: ChartDataPoint = {"NAME": "Test", "vote": 5}
    assert point["NAME"] == "Test"
    assert point["vote"] == 5


def test_chart_data_is_list() -> None:
    """ChartData is a list of ChartDataPoint."""
    data: ChartData = [
        {"NAME": "Alice", "vote": 3},
        {"NAME": "Bob", "vote": 7},
    ]
    assert len(data) == 2
    assert data[0]["NAME"] == "Alice"
