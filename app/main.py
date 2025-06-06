from fastapi import FastAPI
from pydantic import BaseModel
from app.model.nlp import extrair_tributos
from app.schemas import ExtracaoResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir todas as origens (ou especifique as origens confiáveis)
origins = ["*"]  # Ou algo como ["https://meufrontend.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["OPTIONS","POST"],  # ou especifique ["GET", "POST", etc.]
    allow_headers=["*"],
)


class TextoEntrada(BaseModel):
    texto: str

@app.post('/extrair', response_model=ExtracaoResponse)
def extrair(texto_entrada: TextoEntrada):
    resultado = extrair_tributos(texto_entrada.texto)
    return ExtracaoResponse(**resultado) 