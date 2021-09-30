from pydantic import BaseModel, Field
from .car import Car, CarView, move_on
import asyncio
from typing import List, Optional, Any


class Race(BaseModel):
    name: str = Field(..., title="name of the race")
    distance: Optional[int] = Field(..., title="distance of the race", description="The cars will race over this distance. If nothing is set then they will run until their fuel reserve runs out.")
    cars: List[Car] =  Field(..., title="list of cars in the race")


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
