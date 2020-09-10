FROM python:3-alpine3.11 as base

RUN apk --update add openssl ca-certificates

WORKDIR /app
COPY lib /lib/

FROM base as requirements

# C libs needed to build cryptography a dependency for requests
RUN apk --update add libffi-dev openssl-dev build-base

COPY authservice/requirements.txt /app/
RUN pip install --user --no-warn-script-location --no-cache-dir \
                -r /app/requirements.txt
RUN chmod -R oug+r /root/.local
RUN find /root/.local -type d -exec chmod oug+x {} +

FROM base as prod

COPY --from=requirements /root/.local /usr/local
COPY authservice/auth.yaml .
COPY authservice /app/

CMD ["gunicorn", "auth_rest_service:app", "--config", "/app/gunicorn.config.py"]

FROM prod as develop

RUN pip install --user --no-warn-script-location --no-cache-dir \
                -r /app/requirements-dev.txt

FROM prod

LABEL maintainer="wzhu26@illinois.edu"

USER nobody
