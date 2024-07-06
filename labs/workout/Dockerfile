FROM python:3.12-slim-bookworm

COPY requirements.txt .

COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /api

COPY workout_api .
