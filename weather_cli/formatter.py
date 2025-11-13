"""Output formatting utilities for Weather CLI."""

import json
from typing import Dict, Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

from .weather import WeatherData


console = Console()


class WeatherFormatter:
    """Formatter for weather data output."""

    @staticmethod
    def format_json(weather: WeatherData) -> str:
        """
        Format weather data as JSON.

        Args:
            weather: WeatherData object to format.

        Returns:
            JSON string representation of weather data.
        """
        data = {
            "location": {
                "city": weather.city,
                "country": weather.country
            },
            "weather": {
                "description": weather.description,
                "temperature": {
                    "current": weather.temperature,
                    "feels_like": weather.feels_like
                },
                "humidity": weather.humidity,
                "pressure": weather.pressure,
                "wind_speed": weather.wind_speed,
                "cloudiness": weather.clouds
            }
        }
        return json.dumps(data, indent=2)

    @staticmethod
    def format_plain(weather: WeatherData) -> str:
        """
        Format weather data as plain text.

        Args:
            weather: WeatherData object to format.

        Returns:
            Plain text representation of weather data.
        """
        return str(weather)

    @staticmethod
    def format_rich(weather: WeatherData) -> None:
        """
        Format and display weather data with rich formatting.

        Args:
            weather: WeatherData object to format.
        """
        # Create location header
        location = f"{weather.city}, {weather.country}" if weather.country else weather.city

        # Create weather table
        table = Table(show_header=False, box=box.ROUNDED, padding=(0, 2))
        table.add_column("Property", style="cyan bold", no_wrap=True)
        table.add_column("Value", style="white")

        # Determine color based on temperature
        temp_color = "red" if weather.temperature > 30 else "yellow" if weather.temperature > 20 else "blue"

        # Add weather information
        table.add_row("🌤️  Description", weather.description.capitalize())
        table.add_row(
            "🌡️  Temperature",
            f"[{temp_color}]{weather.temperature}°C[/{temp_color}] (feels like {weather.feels_like}°C)"
        )
        table.add_row("💧 Humidity", f"{weather.humidity}%")
        table.add_row("🔽 Pressure", f"{weather.pressure} hPa")
        table.add_row("💨 Wind Speed", f"{weather.wind_speed} m/s")

        # Determine cloud emoji based on cloudiness
        cloud_emoji = "☁️" if weather.clouds > 50 else "⛅" if weather.clouds > 20 else "☀️"
        table.add_row(f"{cloud_emoji} Cloudiness", f"{weather.clouds}%")

        # Display in a panel
        panel = Panel(
            table,
            title=f"[bold green]Weather in {location}[/bold green]",
            border_style="green",
            padding=(1, 2)
        )

        console.print(panel)

    @staticmethod
    def print_error(message: str) -> None:
        """
        Print an error message with formatting.

        Args:
            message: Error message to display.
        """
        console.print(f"[bold red]Error:[/bold red] {message}")

    @staticmethod
    def print_info(message: str) -> None:
        """
        Print an informational message with formatting.

        Args:
            message: Info message to display.
        """
        console.print(f"[blue]ℹ️  {message}[/blue]")

    @staticmethod
    def print_success(message: str) -> None:
        """
        Print a success message with formatting.

        Args:
            message: Success message to display.
        """
        console.print(f"[bold green]✓[/bold green] {message}")
