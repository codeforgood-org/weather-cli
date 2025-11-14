#!/usr/bin/env python3
"""
Basic usage example for Weather CLI.

This example demonstrates how to use the weather_cli package
programmatically in your Python scripts.
"""

import os
from weather_cli.config import Config
from weather_cli.weather import WeatherClient
from weather_cli.formatter import WeatherFormatter


def main():
    """Fetch and display weather for multiple cities."""
    # Ensure API key is set
    if not os.getenv("OPENWEATHER_API_KEY"):
        print("Please set OPENWEATHER_API_KEY environment variable")
        return

    # Cities to check
    cities = ["London", "Tokyo", "New York", "Paris", "Sydney"]

    # Initialize configuration
    config = Config()
    formatter = WeatherFormatter()

    print("Fetching weather for multiple cities...\n")

    # Create weather client
    with WeatherClient(config) as client:
        for city in cities:
            try:
                weather = client.get_weather(city)
                if weather:
                    formatter.format_rich(weather)
                    print()  # Empty line between cities
            except Exception as e:
                formatter.print_error(f"Failed to fetch weather for {city}: {e}")


if __name__ == "__main__":
    main()
