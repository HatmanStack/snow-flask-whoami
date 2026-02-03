"""Type definitions for snow-flask-whoami application."""

from typing import TypedDict


class ChartDataPoint(TypedDict):
    """A single data point for chart visualization."""

    NAME: str
    vote: int


AddressList = list[tuple[str, str]]
ChartData = list[ChartDataPoint]
