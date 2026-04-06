from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Backend is running ✅"}

@app.post("/ask")
def ask(q: Question):
    return {"answer": f"Answer for: {q.question}"}