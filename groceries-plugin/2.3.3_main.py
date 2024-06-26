from fastapi import FastAPI
from pydantic import BaseModel # это обычно отдельный файл модели, код единым текстом для наглядности


app = FastAPI()

class User(BaseModel):
    username: str
    user_info: str

fake_db = [{"username": "vasya", "user_info": "любит колбасу"}, {"username": "katya", "user_info": "любит петь"}]


# тут не меняли
@app.get('/users')
async def get_all_users():
    return fake_db

# тут добавили проверку данных на основании модели, а также указываем модель ответа        
@app.post('/add_user', response_model=User) # тут указали модель (формат) ответа
async def add_user(user: User): # собственно тут проверяем входные данные на соответствие модели
    fake_db.append({"username": user.username, "user_info": user.user_info}) # тут добавили юзера в фейковую БД
    return user