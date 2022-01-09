FROM python:3-alpine

ARG UID=1005
ARG USERNAME=flask

WORKDIR /u01
COPY .  /u01

RUN \
  apk update && \
  apk add build-base && \
  adduser -g ${USERNAME} ${USERNAME} --disabled-password --uid ${UID} && \
  pip install --upgrade pip && \
  pip install -r /u01/requirements.txt

EXPOSE 8080

USER ${USERNAME}

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app" ]
