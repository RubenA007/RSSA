from fastapi import FastAPI, Response
from datetime import datetime

app = FastAPI()

@app.get("/")
def root(response: Response):
    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")  # Get the current date and time
    response.set_cookie(key="last_visit", value=now)  # Set the cookie
    return {"message": "куки установлены"}