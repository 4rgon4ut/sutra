FROM python:3.11-slim-bookworm

# Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install the package
RUN uv pip install --system .

# Run the server
ENTRYPOINT ["python", "-m", "context_engineering_mcp.server"]
