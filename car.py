from pydantic import BaseModel

class Car(BaseModel):
    name: str
    model: str
    weight: int
    length: int
    height: int
    width: int
    maximum_speed: int
    tank_size: int
    average_consumption: int
