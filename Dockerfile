FROM python:3.13.4-slim

ENV PYTHONUNBUFFERED=1 \   
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY marketbridge/requirements.txt .

RUN uv pip install --no-cache-dir -r requirements.txt --system

COPY marketbridge/ .

EXPOSE 8000

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]