FROM python:3.11-slim-buster as builder

ENV APP_HOME=/app \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache


LABEL maintainer='knimako84@gmail.com'
LABEL description="Development image for SSO Project"


RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y python3-dev libpq-dev libpq5 python3-venv \
    && apt-get install -y gettext \
    && apt-get install -y netcat-openbsd gcc postgresql libmagic-dev \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install poetry==1.7.1


WORKDIR $APP_HOME

COPY pyproject.toml poetry.lock ./

RUN mkdir $APP_HOME/staticfiles

# Install project dependencies
RUN poetry config virtualenvs.create false && poetry install && rm -rf $POETRY_CACHE_DIR

# FROM python:3.11-alpine as runtime

# ENV VIRTUAL_ENV=/app/.venv \
#     PATH="/app/.venv/bin:$PATH"

# COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}


# Copy installed python packages and other necessary files from builder to runtime
# COPY --from=builder $APP_HOME $APP_HOME
# Copy the entrypoint and start scripts from the local machine
COPY ./docker/local/django/entrypoint /entrypoint
COPY ./docker/local/django/start /start
COPY ./docker/local/django/celery/worker/start /start-celeryworker
COPY ./docker/local/django/celery/flower/start /start-flower

# Prepare entrypoint and start scripts
RUN sed -i 's/\r$//g' /entrypoint \
    && chmod +x /entrypoint \
    && sed -i 's/\r$//g' /start \
    && chmod +x /start \
    && sed -i 's/\r$//g' /start-celeryworker \
    && chmod +x /start-celeryworker \
    && sed -i 's/\r$//g' /start-flower \
    && chmod +x /start-flower

ENTRYPOINT ["/entrypoint"]