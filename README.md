# extrair-tributos

API para extração de informações tributárias (IR, IOF, PIS, COFINS, CIDE) de textos usando FastAPI e spaCy.

## Como rodar localmente

1. Clone o repositório:
   ```
   git clone https://github.com/eduardomedeiros0510/extrair-tributos.git
   cd extrair-tributos
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Treine ou coloque seu modelo spaCy customizado em `app/model/spacy_model`.

4. Rode a API:
   ```
   uvicorn app.main:app --reload
   ```

## Como usar

- Endpoint: `POST /extract-taxes`
- Body (JSON):
  ```json
  {
    "text": "O valor do IR é R$ 100,00 com alíquota de 15% sobre base de cálculo de R$ 666,00. O IOF é R$ 10,00 com alíquota de 1%."
  }
  ```
- Resposta:
  ```json
  {
    "VALOR_IOF": "R$ 10,00",
    "VALOR_IR": "R$ 100,00",
    "VALOR_PIS": null,
    "VALOR_COFINS": null,
    "VALOR_CIDE": null,
    "ALIQUOTA_IOF": "1%",
    "ALIQUOTA_IR": "15%",
    "BASE_CALCULO_IR": "R$ 666,00"
  }
  ```

## Deploy no GitHub

1. Faça commit dos arquivos e envie para o repositório:
   ```
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

## Deploy no Render

1. Crie uma conta em [Render](https://render.com/).
2. Clique em "New Web Service" e conecte seu repositório GitHub.
3. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
   - Python Version: 3.10+
   - Root Directory: `extrair-tributos`
4. Aguarde o deploy.

## Testando com Postman

- Método: `POST`
- URL: `https://<seu-endpoint-render>.onrender.com/extract-taxes`
- Body (raw, JSON):
  ```json
  {
    "text": "O valor do IR é R$ 100,00 com alíquota de 15% sobre base de cálculo de R$ 666,00. O IOF é R$ 10,00 com alíquota de 1%."
  }
  ``` 