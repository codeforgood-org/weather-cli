# Weather CLI Examples

This directory contains example scripts demonstrating various ways to use the Weather CLI package.

## Examples

### 1. Basic Usage (`basic_usage.py`)

Demonstrates basic programmatic usage of the weather_cli package to fetch weather for multiple cities.

```bash
python examples/basic_usage.py
```

Features:
- Fetching weather for multiple cities
- Using the WeatherClient context manager
- Error handling
- Rich formatted output

### 2. JSON Export (`json_export.py`)

Shows how to fetch weather data and export it to a JSON file with timestamps.

```bash
python examples/json_export.py
```

Features:
- Batch weather data fetching
- JSON file export
- Timestamped data
- Progress indicators

### 3. Temperature Comparison (`temperature_comparison.py`)

Compares temperatures across multiple cities and displays results in a table.

```bash
python examples/temperature_comparison.py
```

Features:
- Multi-city comparison
- Sorted temperature display
- Finding temperature extremes
- Rich table formatting

## Requirements

All examples require:
- An OpenWeatherMap API key set as `OPENWEATHER_API_KEY` environment variable
- The weather_cli package installed

## Running Examples

1. Set up your environment:
```bash
export OPENWEATHER_API_KEY='your_api_key_here'
```

2. Install the package:
```bash
pip install -e .
```

3. Run any example:
```bash
python examples/basic_usage.py
```

## Creating Your Own Scripts

You can use these examples as templates for your own scripts. The basic pattern is:

```python
from weather_cli.config import Config
from weather_cli.weather import WeatherClient

config = Config()
with WeatherClient(config) as client:
    weather = client.get_weather("London")
    print(weather)
```

## Additional Ideas

Here are some ideas for extending these examples:

- **Weather Alerts**: Check if temperature exceeds certain thresholds
- **Historical Tracking**: Store weather data in a database over time
- **Notifications**: Send alerts when conditions change
- **Data Visualization**: Create charts from weather data
- **API Integration**: Use weather data in web applications
- **Automation**: Schedule regular weather checks with cron

## Need Help?

- Check the main [README](../README.md) for more information
- Review the [API documentation](../weather_cli/)
- Open an issue on GitHub if you find problems
