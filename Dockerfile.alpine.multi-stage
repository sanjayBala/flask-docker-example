FROM python:3-alpine as builder

ENV PATH="/opt/venv/bin:${PATH}"

COPY requirements.txt  /u01/requirements.txt

RUN \
  apk update && \
  apk add build-base && \
  python -m venv /opt/venv && \
  pip install --upgrade pip && \
  pip install -r /u01/requirements.txt

FROM python:3-alpine

ARG UID=1005
ARG USERNAME=flask

COPY .  /u01
COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:${PATH}"

RUN \
  apk update && \
  adduser -g ${USERNAME} ${USERNAME} --disabled-password --uid ${UID} && \
  chown -R ${USERNAME} /u01

EXPOSE 8080
WORKDIR /u01

USER ${USERNAME}

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app" ]
