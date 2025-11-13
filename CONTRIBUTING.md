# Contributing to Weather CLI

First off, thank you for considering contributing to Weather CLI! It's people like you that make Weather CLI such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming and inclusive environment. Please be respectful and constructive in your interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if applicable**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any similar features in other tools if applicable**

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the code style guidelines
3. **Add tests** if you've added code that should be tested
4. **Ensure the test suite passes**
5. **Update documentation** as needed
6. **Submit your pull request**

## Development Setup

### Prerequisites

- Python 3.7 or higher
- Git

### Setting Up Development Environment

1. Clone your fork of the repository:
```bash
git clone https://github.com/YOUR_USERNAME/weather-cli.git
cd weather-cli
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

4. Set up your API key:
```bash
cp .env.example .env
# Edit .env and add your OpenWeatherMap API key
```

## Code Style Guidelines

We follow PEP 8 with some modifications:

- **Line length**: Maximum 88 characters (Black default)
- **Imports**: Sorted with isort
- **Type hints**: Use type hints for function signatures
- **Docstrings**: Use Google-style docstrings

### Running Code Quality Tools

Before submitting a pull request, run these tools:

```bash
# Format code with Black
black weather_cli tests

# Sort imports with isort
isort weather_cli tests

# Lint with flake8
flake8 weather_cli tests

# Type check with mypy
mypy weather_cli

# Run all linters (optional)
pylint weather_cli
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=weather_cli --cov-report=html

# Run specific test file
pytest tests/test_weather.py

# Run specific test
pytest tests/test_weather.py::TestWeatherClient::test_get_weather_success
```

### Writing Tests

- Write tests for all new features and bug fixes
- Aim for high code coverage (target: >80%)
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern
- Use fixtures for common test setup
- Mock external API calls

Example test:
```python
def test_get_weather_success(self, monkeypatch):
    """Test successful weather fetch."""
    monkeypatch.setenv("OPENWEATHER_API_KEY", "test_key")
    # ... rest of test
```

## Project Structure

```
weather-cli/
├── weather_cli/          # Main package
│   ├── __init__.py      # Package initialization
│   ├── cli.py           # CLI interface
│   ├── config.py        # Configuration management
│   └── weather.py       # Weather API client
├── tests/               # Test suite
│   ├── test_cli.py
│   ├── test_config.py
│   └── test_weather.py
├── .github/             # GitHub configuration
│   └── workflows/       # CI/CD workflows
├── docs/                # Documentation (if added)
├── requirements.txt     # Production dependencies
├── requirements-dev.txt # Development dependencies
└── pyproject.toml       # Project configuration
```

## Commit Message Guidelines

We follow conventional commit messages:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
```
feat: add support for 5-day forecast
fix: handle connection timeout errors
docs: update README with new examples
test: add tests for config validation
```

## Branch Naming

Use descriptive branch names:

- `feature/feature-name` for new features
- `fix/bug-description` for bug fixes
- `docs/description` for documentation
- `refactor/description` for refactoring

## Release Process

Releases are managed by maintainers:

1. Update version in `__init__.py` and `pyproject.toml`
2. Update CHANGELOG.md
3. Create a git tag
4. Push to PyPI (maintainers only)

## Need Help?

Don't hesitate to ask questions:

- Open an issue with the `question` label
- Reach out to maintainers
- Check existing documentation

## Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- GitHub contributors page

Thank you for contributing!
