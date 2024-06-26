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
    <h1>Это пример html-страницы</h1>
    <p>Я НЕРЕАЛЬНО КРУТ И МОЙ РЕСПЕКТ БЕЗ МЕРЫ :)</p>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(content=html_content, status_code=200)

