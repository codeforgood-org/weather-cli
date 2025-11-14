#!/usr/bin/env python3
"""
Example: Compare temperatures across multiple cities.

This example demonstrates comparing weather data and finding extremes.
"""

import os
from weather_cli.config import Config
from weather_cli.weather import WeatherClient
from rich.console import Console
from rich.table import Table


def main():
    """Compare temperatures across multiple cities."""
    if not os.getenv("OPENWEATHER_API_KEY"):
        print("Please set OPENWEATHER_API_KEY environment variable")
        return

    # Cities to compare
    cities = [
        "London", "Tokyo", "New York", "Paris", "Sydney",
        "Dubai", "Moscow", "Singapore", "Rio de Janeiro"
    ]

    config = Config()
    console = Console()
    weather_data = []

    console.print("\n[bold cyan]Fetching weather data...[/bold cyan]\n")

    with WeatherClient(config) as client:
        for city in cities:
            try:
                weather = client.get_weather(city)
                if weather:
                    weather_data.append(weather)
                    console.print(f"✓ {city}", style="green")
            except Exception as e:
                console.print(f"✗ {city}: {e}", style="red")

    if not weather_data:
        console.print("\n[red]No weather data fetched[/red]")
        return

    # Create comparison table
    table = Table(title="Temperature Comparison")
    table.add_column("City", style="cyan", no_wrap=True)
    table.add_column("Temperature", justify="right", style="yellow")
    table.add_column("Feels Like", justify="right", style="yellow")
    table.add_column("Description", style="green")

    # Sort by temperature
    weather_data.sort(key=lambda x: x.temperature, reverse=True)

    for weather in weather_data:
        location = f"{weather.city}, {weather.country}" if weather.country else weather.city
        table.add_row(
            location,
            f"{weather.temperature}°C",
            f"{weather.feels_like}°C",
            weather.description.capitalize()
        )

    console.print("\n")
    console.print(table)

    # Find extremes
    hottest = max(weather_data, key=lambda x: x.temperature)
    coldest = min(weather_data, key=lambda x: x.temperature)

    console.print(f"\n[red]🔥 Hottest:[/red] {hottest.city} at {hottest.temperature}°C")
    console.print(f"[blue]❄️  Coldest:[/blue] {coldest.city} at {coldest.temperature}°C\n")


if __name__ == "__main__":
    main()
