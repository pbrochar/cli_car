import json
from ._request import _request
from typing import List
from models.race import Race, RaceView
from resources.car import get_cars_by_names


def create_race(race: Race) -> RaceView:
    response = _request(
        url="http://localhost:1337/races",
        method="post",
        data=json.dumps({
            "name": race.name,
            "cars": [
                car.id
                for car in get_cars_by_names([
                        car.name
                        for car in race.cars
                        ])
            ],
            "distance": race.distance,
        }),
        headers={"Content-Type": "application/json"}
    )
    response.raise_for_status()
    return RaceView(**response.json())


def delete_race(id: int) -> None:
    response = _request(
        method="delete",
        url=f"http://localhost:1337/races/{id}",
    )
    response.raise_for_status()


def get_race(id: int) -> RaceView:
    response = _request(
        method="get",
        url=f"http://localhost:1337/races/{id}",
        headers={"Content-Type": "application/json"}
    )
    response.raise_for_status()
    return RaceView(**response.json())


def list_races() -> List[RaceView]:
    response = _request(
        method="get",
        url="http://localhost:1337/races",
        headers={"Content-Type": "application/json"}
    )
    response.raise_for_status()
    return [
        RaceView(**raceview)
        for raceview in response.json()
    ]
