FROM python:3-alpine3.11 as base

RUN apk --update add openssl ca-certificates

WORKDIR /app
COPY lib /lib/

FROM base as requirements

# C libs needed to build cryptography a dependency for requests
RUN apk --update add libffi-dev openssl-dev build-base

COPY auth-middleware-test-svc/requirements.txt /
RUN pip install --user --no-warn-script-location --no-cache-dir \
                -r /requirements.txt
RUN chmod -R oug+r /root/.local
RUN find /root/.local -type d -exec chmod oug+x {} +

FROM base

#########

LABEL maintainer="ywkim@illinois.edu"

COPY --from=requirements /root/.local /usr/local
COPY auth-middleware-test-svc /app/

USER nobody

CMD ["gunicorn", "flaskapp:app", "--config", "/app/gunicorn.config.py"]
