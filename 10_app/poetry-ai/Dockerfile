# Stage 1: Build dependencies
FROM python:3.11-slim as builder

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only necessary files for dependency resolution
COPY pyproject.toml poetry.lock ./

# Install dependencies in a virtual environment
RUN poetry config virtualenvs.create true \
    && poetry install --no-dev

# Copy application source files
COPY . .

# Stage 2: Production image (distroless and rootless)
FROM gcr.io/distroless/python3-debian12:nonroot

# Set working directory
WORKDIR /app

# Copy virtual environment and source files from builder
COPY --from=builder /app /app

# Use virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Switch to non-root user for security
USER nonroot:nonroot

# Command to run the app
CMD ["-m", "poetry_ai.main"]
