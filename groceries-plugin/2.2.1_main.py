from fastapi import FastAPI

app = FastAPI()

# пример роута (маршрута)
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}