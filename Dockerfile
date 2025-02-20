FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SUPABASE_URL=<sua-url-do-supabase>
ENV SUPABASE_API_KEY=<sua-chave-de-api>

EXPOSE 8000

CMD ["python", "-m", "ingestao.ingestao_dados"]
