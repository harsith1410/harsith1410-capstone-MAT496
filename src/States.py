from typing import *

class WeatherData(TypedDict):
    """Represents the global weather conditions for the race."""
    WeatherID: Literal[1, 2]
    Weather: Literal["Dry", "Wet"]


class TrackData(TypedDict):
    """Represents the static data for the selected track."""
    TrackID: Literal[1, 2, 3]
    TrackName: Literal["Monaco", "Great Britain", "Abu Dhabi"]

    Soft_Deg: float
    Medium_Deg: float
    Wet_Deg: float

    Fuel_Consumption: float


class TelemetryData(TypedDict):
    """
    Represents the dynamic telemetry for a single car.

    Note: Removed TrackData and WeatherData from here, as they are
    part of the GlobalState, passed to any node that needs them.
    This avoids redundant and potentially conflicting data.
    """
    Tyre: Literal["Soft", "Medium", "Wet"]
    TyreLaps: int
    TyreDegradation: float
    FuelRemaining: float

    BrakeTemp: float
    engine_mode: str
    drs_available: bool
    laps_remaining: int
    LastLapTime: float


class Car(TypedDict):
    """Represents a single car and its state."""
    CarPosition: int
    CarID: int
    Team: str
    Telemetry: TelemetryData
    Driver: str
    TyreStrat: str
    PitStopLaps: List[int]
    TotalRaceTime: float


class GlobalState(TypedDict):
    Cars: List[Car]
    Track: TrackData
    Weather: WeatherData
    CurrentLap: int
    TotalLaps: int
    RaceOver: bool