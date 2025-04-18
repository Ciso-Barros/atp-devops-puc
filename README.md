# ATP DevOps - Dockerização

Aplicação Flask containerizada para a atividade da PUC.

## Como executar:
```bash
docker build -t atp-api .
docker run -p 5000:5000 atp-api
