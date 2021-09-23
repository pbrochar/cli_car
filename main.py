from error import CarNotFound
from pydantic import ValidationError
from requests.exceptions import HTTPError
import typer
import cli_car
import sys
import requests


app = typer.Typer(add_completion=False, help="CLI for cars races")
app.add_typer(cli_car.app, name="car")

if __name__ == "__main__":
    try:
        app()
    except HTTPError as e:
        if e.response.status_code == 404:
            typer.secho("id not found in database", fg=typer.colors.RED, file=sys.stderr)
        else:
            raise
    except CarNotFound as e:
        typer.secho(f"car with id {e.id} not found in database", fg=typer.colors.RED)
        