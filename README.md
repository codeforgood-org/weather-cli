# Weather CLI 🌤️

A simple, elegant command-line interface for fetching real-time weather information from OpenWeatherMap API.

## Features

- 🌍 Get weather for any city worldwide
- 🌡️ Detailed weather information including temperature, humidity, wind speed, and more
- 🔧 Configurable temperature units (Celsius, Fahrenheit, Kelvin)
- 🔐 Secure API key management via environment variables
- ✨ Clean, modular Python code with type hints
- 🧪 Comprehensive error handling
- 📦 Easy installation and setup

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- An OpenWeatherMap API key ([get one free here](https://openweathermap.org/api))

### Quick Install

1. Clone this repository:
```bash
git clone https://github.com/codeforgood-org/weather-cli.git
cd weather-cli
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
```bash
export OPENWEATHER_API_KEY='your_api_key_here'
```

Or create a `.env` file:
```bash
echo "OPENWEATHER_API_KEY=your_api_key_here" > .env
```

### Package Installation (Optional)

Install as a package for system-wide access:

```bash
pip install -e .
```

## Usage

### Basic Usage

Get weather for a city:

```bash
python -m weather_cli.cli London
```

Or if installed as a package:

```bash
weather-cli London
```

### Multi-word City Names

For cities with spaces in their names:

```bash
python -m weather_cli.cli New York
python -m weather_cli.cli San Francisco
```

### Temperature Units

Choose your preferred temperature unit:

```bash
# Celsius (default)
python -m weather_cli.cli Tokyo

# Fahrenheit
python -m weather_cli.cli Tokyo --units imperial

# Kelvin
python -m weather_cli.cli Tokyo --units standard
```

### Examples

```bash
# Get weather for Paris
$ python -m weather_cli.cli Paris

Weather in Paris, FR:
  Description: Clear sky
  Temperature: 18.5°C (feels like 17.8°C)
  Humidity: 65%
  Pressure: 1015 hPa
  Wind Speed: 3.5 m/s
  Cloudiness: 10%
```

## Development

### Project Structure

```
weather-cli/
├── weather_cli/           # Main package directory
│   ├── __init__.py       # Package initialization
│   ├── cli.py            # Command-line interface
│   ├── config.py         # Configuration management
│   └── weather.py        # Weather data fetching and processing
├── tests/                # Test directory
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_weather.py
│   └── test_cli.py
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
├── README.md             # This file
├── requirements.txt      # Production dependencies
├── requirements-dev.txt  # Development dependencies
└── pyproject.toml        # Project configuration
```

### Running Tests

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=weather_cli --cov-report=html
```

### Code Quality

This project uses various tools to maintain code quality:

```bash
# Format code with black
black weather_cli tests

# Sort imports
isort weather_cli tests

# Lint with flake8
flake8 weather_cli tests

# Type checking with mypy
mypy weather_cli
```

## Configuration

### Environment Variables

- `OPENWEATHER_API_KEY` (required): Your OpenWeatherMap API key
- `WEATHER_UNITS` (optional): Default temperature units (`metric`, `imperial`, or `standard`)

### Getting an API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to API Keys section
4. Generate a new API key
5. Add it to your environment variables

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate and follow the code style guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Built with ❤️ by [codeforgood-org](https://github.com/codeforgood-org)

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/codeforgood-org/weather-cli/issues) page
2. Create a new issue if your problem isn't already listed
3. Provide as much detail as possible including error messages and your environment

## Roadmap

Future enhancements planned:

- [ ] 5-day weather forecast
- [ ] Multiple city comparison
- [ ] Weather alerts and notifications
- [ ] Historical weather data
- [ ] Colorized terminal output
- [ ] JSON output format option
- [ ] Configuration file support

---

Made with Python 🐍
