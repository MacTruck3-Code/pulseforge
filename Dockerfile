FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src/ ./src/

RUN python -m pip install --no-cache-dir . \
    && rm -rf src/pulseforge.egg-info \
    && groupadd --system pulseforge \
    && useradd --system --gid pulseforge --create-home pulseforge

USER pulseforge

ENTRYPOINT ["pulseforge"]