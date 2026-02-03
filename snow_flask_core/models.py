"""Type definitions for snow-flask-whoami application."""
from typing import TypedDict, List, Tuple


class ChartDataPoint(TypedDict):
    """A single data point for chart visualization."""
    NAME: str
    vote: int


AddressList = List[Tuple[str, str]]
ChartData = List[ChartDataPoint]
