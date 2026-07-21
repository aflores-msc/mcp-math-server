FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY . .
RUN uv pip install --system .
EXPOSE 7860
CMD ["python", "mcp_server.py"]
