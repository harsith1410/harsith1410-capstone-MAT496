import random
from src.States import  GlobalState


def generate_race_event(State: GlobalState) -> dict:
    """
    Generates a random race event based on probabilities.
    Returns a RaceEvent dictionary.
    """


    prob_safety_car = 0.02
    prob_vsc = 0.03
    prob_yellow = 0.05

    prob_weather_change = 0.05

    roll = random.random()

    if roll < prob_safety_car:
        return {
            "Event":{"Type": "SAFETY_CAR",
            "Message": f"⚠️ SAFETY CAR DEPLOYED (Lap {State['CurrentLap']})! Bunching up the field.",
            "AffectedCarID": None,
            "Severity": 0.4}
        }


    elif roll < prob_safety_car + prob_vsc:
        return {
            "Event": {
                "Type": "VSC",
                "Message": f"⚠️ VIRTUAL SAFETY CAR (Lap {State['CurrentLap']}). Reduce speed.",
                "AffectedCarID": None,
                "Severity": 0.3
            }
        }


    elif roll < prob_safety_car + prob_vsc + prob_yellow:
        sector = random.choice([1, 2, 3])
        return {
            "Event": {
                "Type": "YELLOW_FLAG",
                "Message": f"YELLOW FLAG in Sector {sector}.",
                "AffectedCarID": None,
                "Severity": 0.1
            }
        }


    weather_roll = random.random()
    if weather_roll < prob_weather_change:
        new_weather = "Wet" if State['Weather'] == "Dry" else "Dry"
        return {
            "Event": {
                "Type": "RAIN_CHANGE",
                "Message": f"🌧️ WEATHER UPDATE: Conditions are changing to {new_weather}!",
                "AffectedCarID": None,
                "Severity": 0.0
            },
            "Weather": new_weather
        }

    return {
        "Event": {
            "Type": "GREEN",
            "Message": "🟢 Track Clear.",
            "AffectedCarID": None,
            "Severity": 0.0
        }
    }


def apply_event_effects(State: GlobalState) -> dict:
    """
    Modifies car telemetry or status based on the event.
    e.g., closing gaps under Safety Car.
    """
    event = State["Event"]
    if event != None:
        cars = State['Cars']
        if event["Type"] == "SAFETY_CAR":
            print(event["Message"])
            if cars:
                cars.sort(key=lambda x: x['TotalRaceTime'])
                leader_time = cars[0]['TotalRaceTime']

                for i, car in enumerate(cars):
                    car['TotalRaceTime'] = leader_time + (i * 0.5)
        elif event["Type"] == "VSC":
            print(event["Message"])
            if cars:
                cars.sort(key=lambda x: x['TotalRaceTime'])

                for i, car in enumerate(cars):
                    car['TotalRaceTime'] = car['Telemetry']['LastLapTime'] * (1 + event["Severity"])
        else:
            print(f"Event: {event['Type']}")
        return {"Cars": cars}
    else:
        return {}

