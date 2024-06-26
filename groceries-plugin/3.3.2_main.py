from typing import Annotated, List
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(x_token: Annotated[List[str] | None, Header()] = None):
    return {"X-Token values": x_token}