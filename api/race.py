from fastapi import APIRouter
from typing import List
from models.race import Race, RaceView
from resources.race import create_race, delete_race, get_race, list_races, start_race


router = APIRouter(
    prefix="/races",
    tags=["races"]
)


@router.post("")
async def create(race: Race) -> RaceView:
    """
    Create a race.
    """
    return create_race(race)


@router.delete("/{id}")
async def delete(id: int) -> None:
    """
    Delete a race.
    """
    return delete_race(id)


@router.get("/{id}")
async def get(id: int) -> RaceView:
    """
    Get one race.
    """
    return get_race(id)


@router.get("")
async def list() -> List[RaceView]:
    """
    List all races.
    """
    return list_races()


@router.post("/{id}/start")
async def start(id: int) -> None:
    """
    Start a race.

    The race takes into consideration:
    - the cars : speed, fuel level
    - the distance (optional) of the race.
    If no distance is defined for this race, the cars run until the end of their gas.
    if a distance is set, cars can be unranked if they run out of fuel before the end of the distance
    """
    await start_race(id)
