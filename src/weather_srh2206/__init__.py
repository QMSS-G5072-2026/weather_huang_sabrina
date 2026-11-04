# read version from installed package
from importlib.metadata import version
__version__ = version("weather_srh2206")

from weather_srh2206.weather_srh2206 import (
    celsius_to_fahrenheit,
    clean_readings,
    summarize_temperatures,
)

__all__ = [
    "celsius_to_fahrenheit",
    "clean_readings",
    "summarize_temperatures",
]