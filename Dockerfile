FROM python:3.11.4-slim-buster
ENV SERVICE_PORT=8000

WORKDIR /app

RUN apt update -qq && apt install -qq --no-install-recommends -y \
    make gcc libffi-dev && \
    pip install poetry && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false
RUN poetry lock --no-update
RUN poetry install --only main

COPY . /app/

ENTRYPOINT ["sh", "start.sh"]