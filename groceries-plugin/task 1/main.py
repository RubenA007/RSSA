from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Пример страницы FastAPI</title>
</head>
<body>
    <h1>Это страница, созданная с помощью FastAPI</h1>
    <p>Привет, мир!</p>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(content=html_content, status_code=200)
