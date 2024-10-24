FROM python:3.12-alpine

RUN apk update && \
    apk add --no-cache bash gcc musl-dev postgresql-dev libpq

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]