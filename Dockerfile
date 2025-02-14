FROM python:3.11.4-slim-bookworm as base

ENV PATH /usr/local/bin:$PATH
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update -qq && apt-get install -qq --no-install-recommends -y \
    gcc libffi-dev \
    && pip install --no-cache-dir poetry==1.8.4 \
    && apt-get remove -y gcc libffi-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install -q --only main --no-cache

COPY . /app

FROM python:3.11.4-slim-bookworm as final

WORKDIR /app

COPY --from=base /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=base /usr/local/bin /usr/local/bin
COPY --from=base /app /app

ENTRYPOINT ["sh", "start.sh"]