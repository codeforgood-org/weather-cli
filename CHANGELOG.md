# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-13

### Added
- Initial release of Weather CLI
- Command-line interface for fetching weather data
- Support for OpenWeatherMap API integration
- Environment variable configuration for API keys
- Comprehensive error handling and validation
- Support for multiple temperature units (Celsius, Fahrenheit, Kelvin)
- Detailed weather information display (temperature, humidity, wind, etc.)
- Full test suite with pytest
- Type hints throughout the codebase
- Modular package structure
- Documentation (README, CONTRIBUTING, CHANGELOG)
- GitHub Actions CI/CD pipeline
- Code quality tools configuration (Black, isort, flake8, mypy)
- MIT License

### Features
- Fetch current weather for any city worldwide
- Display comprehensive weather information
- Context manager support for HTTP client
- Proper timeout handling for API requests
- User-friendly error messages
- Command-line argument parsing with argparse

### Documentation
- Comprehensive README with usage examples
- Contributing guidelines
- Environment variable configuration examples
- Installation instructions
- Development setup guide

### Developer Experience
- Automated testing with pytest
- Code coverage reporting
- Multiple Python version support (3.7-3.12)
- Cross-platform compatibility (Linux, macOS, Windows)
- Pre-configured development dependencies
- Linting and formatting tools

## [Unreleased]

### Planned Features
- 5-day weather forecast
- Multiple city comparison
- Weather alerts and notifications
- Historical weather data
- Colorized terminal output
- JSON output format option
- Configuration file support

---

[1.0.0]: https://github.com/codeforgood-org/weather-cli/releases/tag/v1.0.0
