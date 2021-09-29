from pydantic import BaseModel
from typing import Dict, Optional


class Result(BaseModel):
    time: float
    distance: Optional[float]
    ranked: bool
    car_id: int
    race_id: int


class ResultView(BaseModel):
    id: int
    time: float
    distance: Optional[float]
    ranked: bool
    car: Dict
    race: Dict
