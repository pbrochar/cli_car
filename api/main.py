from fastapi import FastAPI
import sys
import requests

from ..cli_token import get_token, refresh_token
from cli_car import list_car
app = FastAPI()

@app.get("/cars")
async def cars():
    response = requests.get(
		url="http://localhost:1337/cars",
  		headers={
        	"Content-Type": "application/json",
			"Authorization": get_token()
        },
	)
    response.raise_for_status()
    return {"message": response.json()}