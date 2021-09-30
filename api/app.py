from fastapi import FastAPI
from api.car import router as car_router
from api.race import router as race_router

app = FastAPI()
app.include_router(car_router)
app.include_router(race_router)
