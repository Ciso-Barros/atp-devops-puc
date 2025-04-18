FROM python:3.9-slim

WORKDIR /app

# Primeiro copia apenas o requirements.txt para aproveitar o cache
COPY requirements.txt .

# Instala explicitamente o Flask e outras dependências
RUN pip install --no-cache-dir -r requirements.txt

# Depois copia o resto da aplicação
COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]