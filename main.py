from fastapi import FastAPI
from pydantic import BaseModel

class CarModel(BaseModel):
  manufacturer: str
  modelName: str
  cc: int
  onRoadPrice: int

app = FastAPI()


@app.get('/')
def root_api():
  return {
    "message": "Welcome to Rob's Blog"
  }

  
@app.post('/cars')
def add_car(car: CarModel):
  return car
