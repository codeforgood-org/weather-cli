# Weather CLI Dockerfile
# Multi-stage build for optimal image size

# Build stage
FROM python:3.11-slim as builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY requirements.txt .

# Install Python dependencies
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY weather_cli/ ./weather_cli/
COPY setup.py pyproject.toml ./

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Install the package
RUN pip install --no-cache-dir -e .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create a non-root user
RUN useradd -m -u 1000 weatheruser && \
    chown -R weatheruser:weatheruser /app

# Switch to non-root user
USER weatheruser

# Set entrypoint
ENTRYPOINT ["python", "-m", "weather_cli.cli"]

# Default command (can be overridden)
CMD ["--help"]

# Labels
LABEL maintainer="codeforgood-org"
LABEL version="1.0.0"
LABEL description="Weather CLI - A simple command-line weather application"
