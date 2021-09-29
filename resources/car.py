import json
from typing import List
from resources._request import _request
from models.car import Car, CarView
from .error import BadCarName


def create_car(car: Car) -> CarView:
    response = _request(
        method="post",
        url="http://localhost:1337/cars",
        data=json.dumps({**car.dict(by_alias=True)}),
        headers={"Content-Type": "application/json"},
    )
    response.raise_for_status()
    return CarView(**response.json())


def delete_car(id: int) -> None:
    response = _request(
        method="delete",
        url=f"http://localhost:1337/cars/{id}",
        headers={"Content-Type": "application/json"},
    )
    response.raise_for_status()


def get_car(id: int) -> CarView:
    response = _request(
        method="get",
        url=f"http://localhost:1337/cars/{id}",
        headers={"Content-Type": "application/json"},
    )
    response.raise_for_status()
    return CarView(**response.json())


def _get_car_by_name(name: str) -> CarView:
    response = _request(
        method="get",
        url="http://localhost:1337/cars",
        params={"name": name},
    )
    response.raise_for_status()
    if not response.json():
        raise BadCarName
    return CarView(**response.json()[0])


def get_cars_by_names(car_names: List[str]) -> List[CarView]:
    response = _request(
        method="get",
        url="http://localhost:1337/cars",
        params={"name": [
            car_name
            for car_name in car_names
        ]}
    )
    response.raise_for_status()
    return [
        CarView(**car)
        for car in response.json()
    ]


def list_car() -> List[CarView]:
    response = _request(
        method="get",
        url="http://localhost:1337/cars",
        headers={"Content-Type": "application/json"}
    )
    response.raise_for_status()
    return [
        CarView(**carview)
        for carview in response.json()
    ]
