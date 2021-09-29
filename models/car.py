from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from resources.error import OutOfGazError
import asyncio


class Car(BaseModel):
    class Config:
        allow_population_by_field_name = True
    name: str
    model: str
    weight: int
    length: int = Field(..., alias="car_length")
    height: int
    width: int
    maximum_speed: int
    tank_size: int
    average_consumption: int


class CarView(BaseModel):
    id: int
    name: str
    model: str
    weight: int
    length: int = Field(..., alias="car_length")
    height: int
    width: int
    maximum_speed: int
    tank_size: int
    average_consumption: int
    races: Optional[List[Dict[Any, Any]]]


async def move_on(car: Car, duration: Optional[int] = None) -> float:
    maximum_move_time = car.tank_size / car.average_consumption
    if duration is None:
        move_time = maximum_move_time
    elif duration < maximum_move_time:
        move_time = duration
    else:
        await asyncio.sleep(maximum_move_time)
        raise OutOfGazError("No Gaz", move_time=maximum_move_time)
    await asyncio.sleep(move_time)
    return move_time
