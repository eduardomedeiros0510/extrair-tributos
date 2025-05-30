from fastapi import FastAPI, Request
import spacy
import os

app = FastAPI()
MODEL_PATH = os.path.join(os.path.dirname(__file__), "tributario_spacy_model")
nlp = spacy.load(MODEL_PATH)

@app.post("/extrair-tributos")
async def extrair_tributos(request: Request):
    data = await request.json()
    texto = data.get("texto", "")
    doc = nlp(texto)
    resultado = [
        {
            "entidade": ent.label_,
            "texto": ent.text,
            "start": ent.start_char,
            "end": ent.end_char
        }
        for ent in doc.ents
    ]
    return {
        "texto_original": texto,
        "entidades_encontradas": resultado
    }
