FROM python:3.12-alpine3.21

WORKDIR /app

COPY . .

RUN pip install -e . && pip install pytest

CMD ["pytest"]
