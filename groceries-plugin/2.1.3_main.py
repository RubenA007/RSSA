from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    num1: int
    num2: int

@app.post("/calculate")
def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}