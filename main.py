from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/add")
def add_numbers(numbers: Numbers):
    result = numbers.a + numbers.b
    return {"result": result}

@app.post("/subtract")
def subtract_numbers(numbers: Numbers):
    result = numbers.a - numbers.b
    return {"result": result}
@app.get("/")
def root():
    return {"message": "Welcome to the calculator API! Use /add or /subtract endpoints."}