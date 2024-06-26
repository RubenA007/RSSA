from fastapi import FastAPI
from models import User

app = FastAPI()

user_data = {
    "name": "John Doe",
    "id": 1
}

user = User(**user_data)

@app.get("/users")
async def get_user():
    return user.dict()
