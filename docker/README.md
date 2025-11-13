# Docker Usage Guide

This guide explains how to use Weather CLI with Docker.

## Quick Start

### Build the Image

```bash
docker build -t weather-cli:latest .
```

### Run with Docker

```bash
# Get weather for a city
docker run --rm -e OPENWEATHER_API_KEY='your_api_key' weather-cli:latest London

# Get weather with custom units
docker run --rm \
  -e OPENWEATHER_API_KEY='your_api_key' \
  -e WEATHER_UNITS='imperial' \
  weather-cli:latest "New York"

# JSON output
docker run --rm \
  -e OPENWEATHER_API_KEY='your_api_key' \
  weather-cli:latest London --format json
```

## Using Docker Compose

### Basic Usage

1. Create a `.env` file with your API key:
```bash
echo "OPENWEATHER_API_KEY=your_api_key_here" > .env
```

2. Run with docker-compose:
```bash
# Get weather for London (default)
docker-compose run --rm weather-cli

# Get weather for a specific city
docker-compose run --rm weather-cli Tokyo

# Multiple cities with examples
docker-compose --profile examples run --rm weather-multi
```

### Development Mode

Run in development mode with live code updates:

```bash
docker-compose --profile dev run --rm weather-dev
```

## Building Multi-Architecture Images

Build for multiple architectures (ARM and x86):

```bash
# Set up buildx
docker buildx create --use

# Build for multiple platforms
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t weather-cli:latest \
  --push .
```

## Docker Hub Deployment

### Tag and Push

```bash
# Tag the image
docker tag weather-cli:latest your-username/weather-cli:latest
docker tag weather-cli:latest your-username/weather-cli:1.0.0

# Push to Docker Hub
docker push your-username/weather-cli:latest
docker push your-username/weather-cli:1.0.0
```

### Pull and Run from Docker Hub

```bash
docker pull your-username/weather-cli:latest
docker run --rm -e OPENWEATHER_API_KEY='your_api_key' your-username/weather-cli:latest London
```

## Advanced Usage

### Running Examples Inside Container

```bash
# Mount examples and run
docker run --rm \
  -e OPENWEATHER_API_KEY='your_api_key' \
  -v $(pwd)/examples:/app/examples:ro \
  weather-cli:latest python /app/examples/temperature_comparison.py
```

### Saving Output to File

```bash
# Export JSON to file
docker run --rm \
  -e OPENWEATHER_API_KEY='your_api_key' \
  -v $(pwd)/output:/output \
  weather-cli:latest London --format json > output/weather.json
```

### Interactive Shell

```bash
# Run interactive Python shell with weather_cli available
docker run --rm -it \
  -e OPENWEATHER_API_KEY='your_api_key' \
  --entrypoint python \
  weather-cli:latest
```

Then in Python:
```python
from weather_cli.config import Config
from weather_cli.weather import WeatherClient

config = Config()
with WeatherClient(config) as client:
    weather = client.get_weather("Paris")
    print(weather)
```

## Image Details

### Size Optimization

The Dockerfile uses multi-stage builds to minimize image size:
- Build stage: Includes build dependencies
- Runtime stage: Only includes necessary runtime dependencies
- Final image size: ~150-200MB

### Security

- Runs as non-root user (`weatheruser`)
- Minimal base image (python:3.11-slim)
- No unnecessary packages installed
- Build dependencies removed in final image

## Troubleshooting

### API Key Not Working

Make sure your API key is properly set:
```bash
# Check if env var is set
docker run --rm -e OPENWEATHER_API_KEY='your_api_key' weather-cli:latest --help
```

### Permission Denied

If you get permission errors:
```bash
# Run as root (not recommended for production)
docker run --rm --user root -e OPENWEATHER_API_KEY='your_api_key' weather-cli:latest London
```

### Updating the Image

After code changes:
```bash
# Rebuild without cache
docker build --no-cache -t weather-cli:latest .

# Or with docker-compose
docker-compose build --no-cache
```

## CI/CD Integration

### GitHub Actions Example

```yaml
- name: Build Docker image
  run: docker build -t weather-cli:latest .

- name: Test Docker image
  env:
    OPENWEATHER_API_KEY: ${{ secrets.OPENWEATHER_API_KEY }}
  run: docker run --rm -e OPENWEATHER_API_KEY weather-cli:latest London --format json
```

## Best Practices

1. **Always use environment variables** for API keys
2. **Use .env file** for local development
3. **Tag images with versions** for production
4. **Use slim base images** to reduce size
5. **Run as non-root user** for security
6. **Use .dockerignore** to exclude unnecessary files
7. **Implement health checks** for production deployments

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
