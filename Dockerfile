FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY . .

# Create a .venv and install only the dependencies
RUN uv sync --no-install-project

EXPOSE 7860

# Execute the server within the uv environment
CMD ["uv", "run", "mcp_server.py"]
