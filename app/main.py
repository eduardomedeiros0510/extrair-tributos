from fastapi import FastAPI
from pydantic import BaseModel
from app.model.nlp import extrair_tributos
from app.schemas import ExtracaoResponse

app = FastAPI()

class TextoEntrada(BaseModel):
    texto: str

@app.post('/extrair', response_model=ExtracaoResponse)
def extrair(texto_entrada: TextoEntrada):
    resultado = extrair_tributos(texto_entrada.texto)
    return ExtracaoResponse(**resultado) 