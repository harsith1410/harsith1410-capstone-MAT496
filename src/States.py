from typing import *


class TrackData(TypedDict):
    TrackID: Literal[1, 2, 3]
    TrackName: Literal["Monaco", "Great Britain", "Abu Dhabi"]

    Soft_Deg: float
    Medium_Deg: float
    Wet_Deg: float

    Fuel_Consumption: float
    WeatherData: WeatherData


class WeatherData(TypedDict):
    WeatherID: Literal[1, 2]
    Weather: Literal["Dry", "Wet"]


class TelemetryData():
    TrackData: TrackData
    WeatherData: WeatherData

    Tyre: Literal["Soft", "Medium", "Wet"]
    TyreLaps: int

    BrakeTemp: float
    engine_mode: str
    drs_available: bool
    laps_remaining: int


class Car(TypedDict):
    CarPosition: int
    CarID: int
    Team: str
    Telemetry: TelemetryData
    Driver: str
    TyreStrat: str


class GlobalState(TypedDict):
    Cars: List[Car]
    Track: TrackData
    Weather: WeatherData
