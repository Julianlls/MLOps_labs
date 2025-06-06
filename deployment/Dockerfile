FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "main:app"]
