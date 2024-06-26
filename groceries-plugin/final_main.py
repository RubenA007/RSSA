from fastapi import FastAPI, Request, Response, HTTPException, Depends, status, Form
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Optional
import secrets

app = FastAPI()

# Dummy data for example purposes
users_db = {
    "user123": {
        "username": "user123",
        "password": "password123",
        "profile": {"name": "John Doe", "age": 30, "email": "john.doe@example.com"}
    }
}

# Session token storage
session_tokens = {}

# Security scheme for basic HTTP authentication
security = HTTPBasic()

# Route to handle login
@app.post("/login")
def login(response: Response, username: str = Form(...), password: str = Form(...)):
    if username in users_db and users_db[username]["password"] == password:
        # Generate a secure session token
        session_token = secrets.token_hex(16)
        session_tokens[session_token] = username
        # Set a secure HTTP-only cookie
        response.set_cookie(key="session_token", value=session_token, httponly=True)
        return {"message": "Login successful"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

# Dependency to get the current user based on the session token
def get_current_user(request: Request):
    session_token = request.cookies.get("session_token")
    if session_token is None or session_token not in session_tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    username = session_tokens[session_token]
    user = users_db.get(username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return user

# Protected route to get user profile
@app.get("/user")
def get_user_profile(current_user: dict = Depends(get_current_user)):
    return current_user["profile"]