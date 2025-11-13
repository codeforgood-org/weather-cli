.PHONY: install install-dev test coverage lint format clean help

help:
	@echo "Weather CLI - Development Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  install      Install production dependencies"
	@echo "  install-dev  Install development dependencies"
	@echo "  test         Run tests"
	@echo "  coverage     Run tests with coverage report"
	@echo "  lint         Run all linters"
	@echo "  format       Format code with black and isort"
	@echo "  clean        Remove build artifacts and cache files"
	@echo "  run          Run the CLI (usage: make run CITY='London')"
	@echo ""

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

test:
	pytest

coverage:
	pytest --cov=weather_cli --cov-report=html --cov-report=term
	@echo "Coverage report generated in htmlcov/index.html"

lint:
	@echo "Running Black..."
	black --check weather_cli tests
	@echo "Running isort..."
	isort --check-only weather_cli tests
	@echo "Running flake8..."
	flake8 weather_cli tests
	@echo "Running mypy..."
	mypy weather_cli
	@echo "All linters passed!"

format:
	@echo "Formatting with Black..."
	black weather_cli tests
	@echo "Sorting imports with isort..."
	isort weather_cli tests
	@echo "Code formatted!"

clean:
	@echo "Cleaning up..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	@echo "Clean complete!"

run:
	@if [ -z "$(CITY)" ]; then \
		echo "Usage: make run CITY='London'"; \
	else \
		python -m weather_cli.cli $(CITY); \
	fi
