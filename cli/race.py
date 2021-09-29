import typer
import json
import asyncio
from resources.error import BadCarName
from resources.race import create_race, delete_race, get_race, list_races
from resources.car import get_cars_by_names
from resources.result import create_results
from typing import List
from models.car import Car
from models.race import Race, run
from pydantic import ValidationError
from sys import stderr

app = typer.Typer()


@app.command(name="create")
def create(car_names: List[str], distance: int = typer.Option(None, "-d")) -> None:
    typer.echo(typer.style(f"Creating race", fg=typer.colors.GREEN, bold=True))
    try:
        cars = get_cars_by_names(car_names)
        if len(cars) != len(car_names):
            raise BadCarName
        race = Race(
            name=typer.prompt("Race name"),
            distance=distance,
            cars=cars,
        )
        create_race(race)
    except ValidationError as e:
        print(e)
        typer.secho("Error in the creation of race",
                    fg=typer.colors.RED, bold=True, file=stderr)
        return


@ app.command(name="delete")
def delete(id: int) -> None:
    delete_race(id)
    typer.secho(f"Race with id {id} removed", fg=typer.colors.GREEN)


@ app.command(name="get")
def get(id: int) -> None:
    race = get_race(id)
    typer.secho(json.dumps(race.dict(), indent=4))


@ app.command(name="list")
def list() -> None:
    carviews = list_races()
    for carview in carviews:
        print(json.dumps(carview.dict(), indent=4))


@ app.command(name="start")
def start(id: int) -> None:
    race = get_race(id)
    cars = [
        Car(**car.dict())
        for car in race.cars
    ]
    move_times = asyncio.run(run(race))
    create_results(race, move_times)
