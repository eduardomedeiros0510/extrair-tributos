# extrair-tributos

API para extrair informações tributárias (IR, IOF, PIS, COFINS, CIDE, valores, bases de cálculo e alíquotas) de textos usando um modelo spaCy treinado.

## Estrutura do Projeto

- `app/`: Código da API FastAPI
- `data/`: Dados de treino e validação
- `model/`: Modelo spaCy treinado
- `train_spacy.py`: Script de treinamento e validação
- `requirements.txt`: Dependências

## Passos para uso

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Treine o modelo:
   ```bash
   python train_spacy.py
   ```
3. Rode a API:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Teste a API no Postman (endpoint `/extract`).

## Deploy

- Publique no GitHub em `extrair-tributos`.
- Faça deploy no Render apontando para o repositório.

## Exemplo de chamada

POST `/extract`
```json
{
  "text": "O valor do IR é R$ 1000, com alíquota de 15% e base de cálculo de R$ 8000. O IOF foi de R$ 200, alíquota 0,38%."
}
``` 