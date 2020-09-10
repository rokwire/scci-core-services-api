FROM python:3-alpine3.11 as base

RUN apk --update add openssl ca-certificates

WORKDIR /usr/src/app/lib
COPY lib .

FROM base as requirements

# C libs needed to build cryptography a dependency for requests
RUN apk --update add libffi-dev openssl-dev build-base

COPY loggingservice/requirements.txt /
RUN pip install --user --no-warn-script-location --no-cache-dir \
                -r /requirements.txt
RUN chmod -R oug+r /root/.local
RUN find /root/.local -type d -exec chmod oug+x {} +

FROM base

LABEL maintainer="ywkim@illinois.edu"

EXPOSE 5000

COPY --from=requirements /root/.local /usr/local

WORKDIR /usr/src/app/loggingservice

COPY loggingservice .

WORKDIR /usr/src/app/loggingservice/api

COPY loggingservice/logging.yaml .

#ENV LOGGING_MONGO_URL=""
ENV LOGGING_URL_PREFIX=""

USER nobody

CMD ["gunicorn", "logging_rest_service:app", "--config", "/usr/src/app/loggingservice/api/gunicorn.config.py"]
