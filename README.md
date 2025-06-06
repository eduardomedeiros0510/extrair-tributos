# extrair-tributos

API para extração de informações tributárias (IR, IOF, PIS, COFINS, CIDE, valores, bases de cálculo e alíquotas) usando modelo spaCy NER.

## Instalação

```bash
pip install -r requirements.txt
```

## Treinamento do Modelo

```bash
python app/model/train.py
```

## Execução da API

```bash
uvicorn app.main:app --reload
```
Acesse a documentação em http://localhost:8000/docs

## Publicação no GitHub

1. Crie o repositório no GitHub: extrair-tributos
2. No terminal:
   ```sh
   git init
   git remote add origin https://github.com/eduardomedeiros0510/extrair-tributos.git
   git add .
   git commit -m "Initial commit"
   git push -u origin master
   ```

## Deploy no Render

1. Crie um novo serviço web no Render.
2. Conecte ao repositório GitHub `extrair-tributos`.
3. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
   - Python Version: 3.10+
4. O serviço ficará disponível em `https://<nome-do-servico>.onrender.com`

## Exemplo de Uso no Postman

- **Endpoint:** `POST /extract`
- **URL:** `https://<nome-do-servico>.onrender.com/extract`
- **Body (JSON):**
  ```json
  {
    "text": "ALIQ IOF: 4.73% | NAVIO: VINICIUS TRADER | DI 640452073 | VALOR DO COFINS: R$ 16.22 | VALOR IR: R$ 439.61 | ALIQUOTA IR: 22.11% | VALOR PISS: R$ 19.33 | DUE 2176985915 | BASE IR: R$ 700.95 | VALOR IOF: R$ 14.85"
  }
  ```
- **Resposta esperada:**
  ```json
  {
    "VALOR_IOF": "14.85",
    "VALOR_IR": "439.61",
    "VALOR_PIS": "19.33",
    "VALOR_COFINS": "16.22",
    "VALOR_CIDE": null,
    "ALIQUOTA_IOF": "4.73",
    "ALIQUOTA_IR": "22.11",
    "BASE_CALCULO_IR": "700.95"
  }
  ``` 