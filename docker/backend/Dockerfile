FROM python:3.10.10-bullseye

ENV PATH /root/.local/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ["./backend/pyproject.toml", "./backend/poetry.lock", "/app/"]

RUN apt-get update \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.in-project true \
    && poetry install

# デフォルトのホストはlocalhost
# 0.0.0.0で解放しないとコンテナ外部からアクセスできない
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]