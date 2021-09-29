import json
from ._request import _request
from typing import List, Dict, Any, Union
from .error import OutOfGazError
from .car import _get_car_by_name
from models.race import Race
from models.result import Result, ResultView


def is_ranked(move_time: Union[float, OutOfGazError]) -> bool:
    return not isinstance(move_time, OutOfGazError)


def create_results(race: Race, move_times: List[Any]) -> None:
    print(race)
    results = [
        Result(
            time=move_time if is_ranked(
                move_time) is True else move_time.move_time,
            distance=race.distance if is_ranked(
                move_time) is True else move_time.move_time * car.maximum_speed,
            ranked=is_ranked(move_time),
            car_id=_get_car_by_name(car.name).id,
            race_id=race.id
        )
        for move_time, car in zip(move_times, race.cars)
    ]
    for result in results:
        create_result(result)


def create_result(result: Result) -> ResultView:
    response = _request(
        method="post",
        url="http://localhost:1337/results",
        data=json.dumps({
            'time': result.time,
            'distance': result.distance,
            'ranked': result.ranked,
            'car': result.car_id,
            'race': result.race_id,
        }),
        headers={'Content-Type': 'application/json'}
    )
    print(response.json())
    response.raise_for_status()
    return (ResultView(**response.json()))
