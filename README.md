# extrair-tributos

API para extração de informações tributárias (IR, IOF, PIS, COFINS, CIDE) de textos utilizando FastAPI e spaCy.

## Como rodar localmente

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Como publicar no GitHub
1. Crie um repositório chamado `extrair-tributos`.
2. Faça commit de todos os arquivos e dê push para o GitHub.

## Como publicar no Render
1. Faça login em [Render](https://render.com/).
2. Crie um novo serviço web, conecte ao repositório do GitHub.
3. Configure o comando de inicialização: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
4. Defina o diretório raiz como `extrair-tributos`. 