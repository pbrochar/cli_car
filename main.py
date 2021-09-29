from resources.error import BadCarName, BadTokenError, CarNotFound
from requests.exceptions import HTTPError
import typer
from cli.car import app as car_app
from cli.race import app as race_app
from sys import stderr


app = typer.Typer(add_completion=False, help="CLI for cars races")
app.add_typer(car_app, name="car")
app.add_typer(race_app, name="race")

if __name__ == "__main__":
    try:
        app()
    except HTTPError as e:
        if e.response.status_code == 404:
            typer.secho("id not found in database",
                        fg=typer.colors.RED, file=stderr)
        elif e.response.status_code == 401:
            typer.secho("Invalid Token")
        else:
            raise
    except CarNotFound as e:
        typer.secho(f"car with id {e.id} not found in database", fg=typer.colors.RED)
    except BadCarName:
        typer.secho("Bad car name")
    except BadTokenError:
        typer.secho("Bad Token")
