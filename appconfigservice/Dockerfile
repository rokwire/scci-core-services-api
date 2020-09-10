FROM python:3-alpine3.11 as base

RUN apk --update add openssl ca-certificates

WORKDIR /app
COPY lib /lib/

FROM base as requirements

# C libs needed to build cryptography a dependency for requests
RUN apk --update add libffi-dev openssl-dev build-base

COPY appconfigservice/requirements.txt appconfigservice/
RUN pip install --user --no-warn-script-location --no-cache-dir \
                -r appconfigservice/requirements.txt
RUN chmod -R oug+r /root/.local
RUN find /root/.local -type d -exec chmod oug+x {} +

FROM base

COPY --from=requirements /root/.local /usr/local
COPY appconfigservice ./appconfigservice
COPY appconfigservice/appconfig.yaml .

ENV APP_CONFIG_MONGO_URL=""
ENV APP_CONFIG_URL_PREFIX=""

WORKDIR /app/appconfigservice/api
VOLUME /var/cache/app

LABEL maintainer="wzhu26@illinois.edu"

USER nobody

CMD ["gunicorn", "appconfig_rest_service:app", "--config", "../gunicorn.config.py"]
