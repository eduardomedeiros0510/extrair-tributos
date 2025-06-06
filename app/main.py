from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.utils import extract_tax_info

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/extract-taxes")
async def extract_taxes(request: TextRequest):
    result = extract_tax_info(request.text)
    return result 