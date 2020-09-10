FROM python:3-alpine3.11 as base

RUN apk --update add openssl ca-certificates

WORKDIR /app
COPY lib /lib/

FROM base as requirements

# C libs needed to build cryptography a dependency for requests
RUN apk --update add libffi-dev openssl-dev build-base

COPY eventservice/requirements.txt /app/eventservice/
RUN pip install --user --no-warn-script-location --no-cache-dir \
                -r /app/eventservice/requirements.txt
RUN chmod -R oug+r /root/.local
RUN find /root/.local -type d -exec chmod oug+x {} +

FROM base

RUN mkdir -p /app/eventservice/events-images/

COPY --from=requirements /root/.local /usr/local
COPY eventservice/events.yaml /app/
COPY eventservice /app/eventservice/

VOLUME /var/cache/app
WORKDIR /app/eventservice/api

LABEL maintainer="bing@illinois.edu"

USER nobody

CMD ["gunicorn", "events_rest_service:app", "--config", "/app/eventservice/api/gunicorn.config.py"]
