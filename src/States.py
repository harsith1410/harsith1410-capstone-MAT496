from typing import *

class TrackData(TypedDict):
    """Represents the static data for the selected track."""
    TrackID: Literal[1, 2, 3]
    TrackName: Literal["Monaco", "Great Britain", "Abu Dhabi"]

    Soft_Deg: float
    Medium_Deg: float
    Hard_Deg: float
    Wet_Deg: float

    Soft_Lap: float
    Medium_Lap: float
    Hard_Lap: float
    Wet_Lap: float

    PitLoss: float
    FuelLoss: float
    TotalFuel: float



class TelemetryData(TypedDict):
    """
    Represents the dynamic telemetry for a single car.
    """
    Tyre: Literal["Soft","Medium","Hard","Wet"]
    TyreLaps: int
    TyreDegradation: float
    laps_remaining: int
    LastLapTime: float
    FuelRemaining: float


class Car(TypedDict):
    """Represents a single car and its state."""
    CarPosition: int
    CarID: int
    Team: str
    Telemetry: Optional[TelemetryData]
    Driver: str
    TotalRaceTime: float
    SpeedDelta: float
    isUser: bool


class RaceEvent(TypedDict):
    Type: Literal["GREEN", "YELLOW_FLAG", "SAFETY_CAR", "VSC", "RAIN_CHANGE"]
    Message: str
    AffectedCarID: Optional[int]
    Severity: float


class GlobalState(TypedDict):
    """This is the Global State of the Graph"""

    Cars: List[Car]
    UserCar: Car
    Weather: Literal["Dry","Wet"]
    Track: TrackData
    CurrentLap: int
    TotalLaps: int
    RaceOver: bool
    Event: RaceEvent


