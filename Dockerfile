FROM python:3.11-slim-bookworm

# Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install the package and uvicorn for HTTP support
RUN uv pip install --system . uvicorn

# Expose the default port
EXPOSE 8000

# Run the server (default to stdio, but overrideable by smithery.yaml)
ENTRYPOINT ["python", "-m", "context_engineering_mcp.server"]
