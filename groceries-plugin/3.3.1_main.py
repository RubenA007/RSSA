from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def root(response: Response):
    response.headers["Secret-Code"] = "123459"
    return {"message": "Hello from my api"}