import sys
import json
import typer
from pydantic import ValidationError
from models.car import Car
from resources.car import create_car, delete_car, get_car, list_car

app = typer.Typer()


@app.command(name="create")
def create() -> None:
    typer.echo(typer.style(f"Creating car", fg=typer.colors.GREEN, bold=True))
    try:
        car = Car(
            name=typer.prompt("Name"),
            model=typer.prompt("Model"),
            weight=typer.prompt("Weight"),
            length=typer.prompt("Lenght"),
            height=typer.prompt("Height"),
            width=typer.prompt("Width"),
            maximum_speed=typer.prompt("Maximum speed"),
            tank_size=typer.prompt("Tank size"),
            average_consumption=typer.prompt("Average consumption"),
        )
    except ValidationError:
        typer.secho("Error in the creation of car",
                    fg=typer.colors.RED, bold=True, file=sys.stderr)
        return
    create_car(car)


@app.command(name="delete")
def delete(id: int) -> None:
    delete_car(id)
    typer.secho(f"car with id {id} removed", fg=typer.colors.GREEN)


@app.command(name="get")
def get(id: int) -> None:
    car = get_car(id)
    typer.secho(json.dumps(car.dict(), indent=4))


@app.command(name="list")
def list() -> None:
    cars = list_car()
    for car in cars:
        print(json.dumps(car.dict(), indent=4))
