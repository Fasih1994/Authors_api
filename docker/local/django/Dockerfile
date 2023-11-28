ARG PYTHON_VERSION=3.11.6-bullseye


FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential libpq-dev

COPY ./requirements  .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt


FROM python as python-run-stage
ARG BUILD_ENVIRONMENT=local

ARG APP_HOME=/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHOUNBUFFERED 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev gettext

RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false

RUN rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheels/ /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/*
RUN rm -rf /wheels/

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY . ${APP_HOME}

ENTRYPOINT [ "/entrypoint" ]