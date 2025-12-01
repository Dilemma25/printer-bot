FROM python:3.12-alpine AS base

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

FROM base AS prod

COPY . .