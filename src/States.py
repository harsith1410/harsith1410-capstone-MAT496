from typing import *

class TrackData(TypedDict):
    """Represents the static data for the selected track."""
    TrackID: Literal[1, 2, 3]
    TrackName: Literal["Monaco", "Great Britain", "Abu Dhabi"]

    Soft_Deg: float
    Medium_Deg: float
    Wet_Deg: float



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
    laps_remaining: int
    LastLapTime: float


class Car(TypedDict):
    """Represents a single car and its state."""
    CarPosition: int
    CarID: int
    Team: Literal["McLaren","RedBull","Mercedes"]
    Telemetry: Optional[TelemetryData]
    Driver: str
    TotalRaceTime: float
    isUser: bool


class GlobalState(TypedDict):
    """This is the Global State of the Graph"""

    Cars: List[Car]
    Track: TrackData
    Weather: Literal["Dry","Wet"]
    CurrentLap: int
    TotalLaps: int
    RaceOver: bool

