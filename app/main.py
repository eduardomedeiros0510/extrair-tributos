from fastapi import FastAPI
from app.schemas import ExtractRequest, ExtractResponse
from app.model.infer import extract_tributos, load_model

app = FastAPI(title="Extrair Tributos API")

nlp = None

@app.on_event("startup")
def load_spacy_model():
    global nlp
    nlp = load_model()

@app.post("/extract", response_model=ExtractResponse)
def extract(request: ExtractRequest):
    result = extract_tributos(request.text, nlp)
    return result 