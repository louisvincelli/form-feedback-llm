from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import openai
import os

from form_feedback.form_prompt import generate_physical_therapist_prompt
from form_feedback.response_formatter import format_response_blocks

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class FormIssue(BaseModel):
    rep: int
    issue: str

class FormData(BaseModel):
    user: str
    exercise: str
    rep_count: int
    form_issues: List[FormIssue]
    mobility_flags: List[str] = []
    experience_level: str

@app.post("/generate-feedback/")
async def generate_feedback(data: FormData):
    try:
        prompt = generate_physical_therapist_prompt(data.dict())

        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a physical therapist AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        response = completion.choices[0].message.content
        structured = format_response_blocks(response)

        return {
            "raw_response": response,
            "structured_response": structured
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
