from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Feedback(BaseModel):
    name: str
    message: str

feedback_list = []

@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    feedback_list.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}!"}