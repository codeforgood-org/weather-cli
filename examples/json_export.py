#!/usr/bin/env python3
"""
Example: Export weather data to JSON file.

This example shows how to fetch weather data and save it to a JSON file.
"""

import os
import json
from datetime import datetime
from weather_cli.config import Config
from weather_cli.weather import WeatherClient


def main():
    """Fetch weather and save to JSON file."""
    if not os.getenv("OPENWEATHER_API_KEY"):
        print("Please set OPENWEATHER_API_KEY environment variable")
        return

    cities = ["London", "Tokyo", "New York"]
    config = Config()
    results = []

    print("Fetching weather data...")

    with WeatherClient(config) as client:
        for city in cities:
            try:
                weather = client.get_weather(city)
                if weather:
                    results.append({
                        "city": weather.city,
                        "country": weather.country,
                        "description": weather.description,
                        "temperature": weather.temperature,
                        "feels_like": weather.feels_like,
                        "humidity": weather.humidity,
                        "pressure": weather.pressure,
                        "wind_speed": weather.wind_speed,
                        "cloudiness": weather.clouds,
                        "timestamp": datetime.now().isoformat()
                    })
                    print(f"✓ Fetched data for {city}")
            except Exception as e:
                print(f"✗ Failed to fetch data for {city}: {e}")

    # Save to file
    filename = f"weather_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n✓ Weather data saved to {filename}")


if __name__ == "__main__":
    main()
