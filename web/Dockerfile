FROM python:3.8-alpine AS base

LABEL maintainer="Realize Security Ltd."

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Create virtualenv path and add to front of $PATH
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt /requirements.txt


WORKDIR /app

RUN apk add --no-cache python3-dev openssl-dev libffi-dev gcc && \
    pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home janus && \
    mkdir -p /vol/static && \
    mkdir -p /vol/log && \
    chown -R janus:janus /vol/static && \
    chown -R janus:janus /vol/log

COPY . /app

RUN /bin/cp -r /app/app/static/* /vol/static

RUN chmod -R 0755 \
    /app \
    /vol/static

VOLUME [ "/vol/static", "/vol/log" ]

COPY ./scripts /app/scripts
RUN chmod +x /app/scripts/run.sh

# DEBUG BUILD
FROM base AS debug

COPY /dev-requirements.txt /dev-requirements.txt
RUN pip install -r /dev-requirements.txt
USER janus
ENTRYPOINT [ "python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "-m", "flask", "run", "--host=0.0.0.0"]


# DEV BUILD
FROM base AS dev

USER janus
ENTRYPOINT [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]

# PROD BUILD
FROM base AS prod

USER janus
ENTRYPOINT [ "python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "manage:app" ]