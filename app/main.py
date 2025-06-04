from fastapi import FastAPI
from app.schema import ExtractRequest, ExtractResponse
from app.model import TributaryExtractor

app = FastAPI()
extractor = TributaryExtractor()

@app.post("/extract", response_model=ExtractResponse)
def extract_tributary_info(request: ExtractRequest):
    result = extractor.extract(request.text)
    return ExtractResponse(**result) 