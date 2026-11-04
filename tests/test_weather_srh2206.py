import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

import weather_srh2206
from weather_srh2206 import (
    celsius_to_fahrenheit,
    clean_readings,
    summarize_temperatures,
)

def test_version_is_defined():
    assert isinstance(weather_srh2206.__version__, str)

@pytest.mark.parametrize("celsius, expected", [
    (0, 32.0),            # freezing point
    (100, 212.0),         # boiling point
    (-40, -40.0),         # the two scales meet here
    (37, 98.6),           # body temperature
    (19.3, 66.74),        # a non-round value
    (-273.15, -459.67),   # absolute zero itself
])
def test_celsius_to_fahrenheit(celsius, expected):
    """Known Celsius values convert to the right Fahrenheit value."""
    result = celsius_to_fahrenheit(celsius)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize("bad_input, expected_error", [
    ("hot", TypeError),     # a string
    (None, TypeError),      # None
    (True, TypeError),      # bool is rejected
    ([20.0], TypeError),    # a list
    (-273.16, ValueError),  # just below absolute zero
    (-500, ValueError),     # far below absolute zero
])
def test_celsius_to_fahrenheit_invalid(bad_input, expected_error):
    """Bad types raise TypeError; impossible temperatures raise ValueError."""
    with pytest.raises(expected_error):
        celsius_to_fahrenheit(bad_input)


def test_summarize_temperatures():
    """NaN values are ignored and counted in n_missing."""
    # Arrange
    temps = [10.0, float("nan"), 20.0, 30.0]

    # Act
    result = summarize_temperatures(temps)

    # Assert
    assert set(result) == {"mean", "min", "max", "n_missing"}
    assert result["mean"] == pytest.approx(20.0)
    assert result["min"] == pytest.approx(10.0)
    assert result["max"] == pytest.approx(30.0)
    assert result["n_missing"] == 1


def test_summarize_temperatures_all_missing():
    """A list with only NaN values has no valid readings."""
    with pytest.raises(ValueError):
        summarize_temperatures([float("nan"), float("nan")])


def test_summarize_temperatures_empty():
    """An empty list has no valid readings."""
    with pytest.raises(ValueError):
        summarize_temperatures([])


@pytest.fixture
def raw_readings():
    """Return the unsorted station DataFrame with one NaN and one 999 error code."""
    return pd.DataFrame({
        "station": ["JFK", "CPK", "JFK", "CPK", "LGA"],
        "date": ["2026-07-02", "2026-07-01", "2026-07-01", "2026-07-02", "2026-07-01"],
        "temp_c": [30.0, 25.0, float("nan"), 999.0, 28.0],
    })


def test_raw_readings_fixture(raw_readings):
    """Check the fixture has the columns, number of rows, and missing values we expect."""
    assert list(raw_readings.columns) == ["station", "date", "temp_c"]
    assert len(raw_readings) == 5
    assert raw_readings["temp_c"].isna().sum() == 1


def _expected_clean():
    """Hand-built result of cleaning raw_readings."""
    return pd.DataFrame({
        "station": ["CPK", "JFK", "LGA"],
        "date": ["2026-07-01", "2026-07-02", "2026-07-01"],
        "temp_c": [25.0, 30.0, 28.0],
        "temp_f": [77.0, 86.0, 82.4],
    })


def test_clean_readings(raw_readings):
    """Drop rows with NaN or 999 C, add temp_f, and sort rows."""
    # Act
    result = clean_readings(raw_readings)

    # Assert
    assert_frame_equal(result, _expected_clean())