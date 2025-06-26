FROM python:3.10.12-slim-buster

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/

WORKDIR /apps/backend

COPY ./apps/backend .

RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x /apps/backend/entrypoint.sh

CMD [ "/apps/backend/entrypoint.sh" ]