from fastapi import APIRouter
from typing import List
from models.car import Car, CarView
from resources.car import list_car, get_car as get_car_view, delete_car, create_car


router = APIRouter(
    prefix="/cars",
    tags=["cars"]
)


@router.post("")
async def create(car: Car) -> CarView:
    """
    Create a car.
    """
    return create_car(car)


@router.delete("/{id}")
async def delete(id: int) -> None:
    """
    Delete a car.
    """
    return delete_car(id)


@router.get("/{id}", response_model=CarView)
async def get_car(id: int) -> CarView:
    """
    Get one car.
    """
    return get_car_view(id)


@router.get("")
async def get() -> List[CarView]:
    """
    List all cars.
    """
    return list_car()
