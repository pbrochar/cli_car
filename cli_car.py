import typer
from pydantic import ValidationError
from error import CarNotFound
from car import Car
from cli_token import token
import requests
import sys
import json

app = typer.Typer()

@app.command(name="create")
def create() -> None:
    typer.echo(typer.style(f"Creating car", fg=typer.colors.GREEN, bold=True))
    try:
        car = Car(
            name= typer.prompt("Name"),
            model= typer.prompt("Model"),
            weight= typer.prompt("Weight"),
            length= typer.prompt("Lenght"),
            height= typer.prompt("Height"),
            width= typer.prompt("Width"),
            maximum_speed= typer.prompt("Maximum speed"),
            tank_size= typer.prompt("Tank size"),
            average_consumption= typer.prompt("Average consumption"),
    )
    except ValidationError as e:
        typer.secho("Error in the creation of car", fg=typer.colors.RED, bold=True, file=sys.stderr)
        return
    response = requests.post(
        url= "http://localhost:1337/cars",
        data=json.dumps({
            "name": car.name,
            "model": car.model,
            "weight": car.weight,
            "car_length": car.length,
            "height": car.height,
            "width": car.width,
            "maximum_speed": car.maximum_speed,
            "tank_size": car.tank_size,
            "average_consumption": car.average_consumption,
        }),
        headers={
            "Authorization": token,
            "Content-Type": "application/json",
        }
    )

@app.command(name="delete")
def delete(id: int) -> None:
    response = requests.delete(
			url=f"http://localhost:1337/cars/{id}",
			headers={"Authorization": token},
    )
    response.raise_for_status()
    typer.secho(f"id {id} removed", fg=typer.colors.GREEN)

@app.command(name="get")
def get_car(id: int) -> None:
    response = requests.get(
        url=f"http://localhost:1337/cars/{id}",
        headers={
            "Authorization": token,
            "Content-Type": "application/json",    
        }
    )
    response.raise_for_status()
    typer.secho(json.dumps(response.json(), indent=4))

@app.command(name="list")
def list_car() -> None:
    response = requests.get(
        url="http://localhost:1337/cars",
        headers={
            "Authorization": token,
            "Content-Type": "application/json",    
        }
    )
    print(json.dumps(response.json(), indent=4))