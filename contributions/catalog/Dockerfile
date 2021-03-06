FROM python:3-alpine3.12

LABEL maintainer="<ywkim@illinois.edu>, <wzhu26@illinois.edu>"

EXPOSE 5050

WORKDIR /usr/src/app/catalog

COPY catalog .

RUN apk --update add python3 py3-pip openssl ca-certificates py3-openssl && \
  apk --update add --virtual build-dependencies libffi-dev openssl-dev python3-dev py3-pip musl-dev cargo build-base && \
  pip install --upgrade pip && \
  pip install -r requirements.txt --no-cache-dir && \
  apk del build-dependencies

WORKDIR /usr/src/app/catalog

ENV CONTRIBUTION_BUILDING_BLOCK_URL='' \
    DB_NAME='' \
    GITHUB_CLIENT_ID='' \
    GITHUB_CLIENT_SECRET='' \
    AUTHORIZATION_BASE_URL='https://github.com/login/oauth/authorize' \
    TOKEN_URL='https://github.com/login/oauth/access_token' \
    AUTHENTICATION_TOKEN='' \
    URL_PREFIX='' \
    DEBUG='False'

CMD ["gunicorn", "catalog_rest_service:app", "--config", "/usr/src/app/catalog/gunicorn.config.py"]