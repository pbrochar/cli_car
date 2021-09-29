from pydantic import BaseModel
from .car import Car, CarView, move_on
from resources.error import OutOfGazError
import asyncio
from typing import List, Optional, Dict, Any


class Race(BaseModel):
    name: str
    distance: Optional[int]
    cars: List[Car]


class RaceView(BaseModel):
    id: int
    name: str
    distance: Optional[int]
    cars: List[CarView]


async def run(race: Race) -> List[Any]:
    move_times = await asyncio.gather(*[
        move_on(car, duration=None if race.distance is None else race.distance /
                car.maximum_speed)
        for car in race.cars
    ], return_exceptions=True)
    return move_times
