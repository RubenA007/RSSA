from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item: # тут мы передали в наш обработчик Pydantic модель, чтобы она проверяла все запросы на соответствие этой модели (все поля и типы данных в них должны соответствовать модели
    return item


@app.get("/items/")
async def read_items() -> list[Item]: # тут мы не принимаем никаких данных, но указываем, что возвращаться будет список, содержащий в себе Pydantic модели    
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ] 