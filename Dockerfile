FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml uv.lock README.md LICENSE ./
COPY common ./common
COPY gym ./gym
COPY scripts ./scripts
COPY apps ./apps
COPY data ./data
RUN pip install --no-cache-dir uv==0.13.7 && uv sync --locked --no-dev --extra apps --extra persistence
RUN useradd --create-home learner && mkdir /app/workspace && chown learner:learner /app/workspace
USER learner
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
EXPOSE 8000
CMD ["/app/.venv/bin/uvicorn", "apps.server:build_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
