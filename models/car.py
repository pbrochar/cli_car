from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from resources.error import OutOfGazError
import asyncio


class Car(BaseModel):
    class Config:
        allow_population_by_field_name = True
    name: str = Field(..., title="name of the car", description="the name of the car must be unique.")
    model: str = Field(..., title="model of the car")
    weight: int = Field(..., title="weight of the car", description="can't be a negative value")
    length: int = Field(..., alias="car_length", title="length of the car", description="can't be a negative value")
    height: int = Field(..., title="height of the car", description="can't be a negative value")
    width: int = Field(..., title="width of the car", description="can't be a negative value")
    maximum_speed: int = Field(..., title="maximum speed of the car", description="can't be a negative value")
    tank_size: int = Field(..., title="tank size of the car", description="can't be a negative value")
    average_consumption: int = Field(..., title="average consumption of the car", description="can't be a negative value")


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
