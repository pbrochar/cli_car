import requests
from requests.exceptions import HTTPError
import os
import typer


def _request_token() -> str:
    status_code = 0
    while status_code != 200:
        identifier = typer.prompt("identifier")
        password = typer.prompt("password", hide_input=True)
        auth = requests.post(
            url="http://localhost:1337/auth/local",
            data={
                'identifier': identifier,
                'password': password,
            }
        )
        try:
            auth.raise_for_status()
        except HTTPError as e:
            if e.response.status_code != 400:
                raise
        status_code = auth.status_code
    token = 'Bearer ' + auth.json()['jwt']
    return token


def refresh_token() -> str:
    try:
        token = _request_token()
    except:
        raise
    with open("token", "w") as file:
        file.write(token)
    return token


def get_token() -> str:
    if not os.path.isfile('./token'):
        token = refresh_token()
    else:
        with open('token', 'r') as token_file:
            token = token_file.read()
    return token
