from fastapi import FastAPI


app = FastAPI()

@app.get('/{user_id}') # тут объявили параметр пути
async def search_user_by_id(user_id: int): # тут указали его тип данных
    # какая-то логика работы поиска
    return {"вы просили найти юзера с id": user_id}