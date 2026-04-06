from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": q.question}
            ],
            max_tokens=150
        )

        answer = response.choices[0].message.content
        return {"answer": answer}

    except Exception as e:
        return {"answer": f"Error: {str(e)}"}
