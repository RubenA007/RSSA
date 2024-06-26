from fastapi import FastAPI


app = FastAPI()

fake_db = [{"username": "vasya", "user_info": "любит колбасу"}, {"username": "katya", "user_info": "любит петь"}]

@app.get('/users') # маршрут GET для ПОЛУЧЕНИЯ каких-то данных с сервера
async def get_all_users():
    return fake_db
    
@app.post('/add_user') # маршрут POST для отправления какой-то информации на сервер
async def add_user(username: str, user_info: str): # принимает два query-параметра, про которые будет рассказано дальше в этом уроке (это не типичный пример пост-запроса)
    fake_db.append({"username": username, "user_info": user_info})
    return {"message": "юзер успешно добавлен в базу данных"}