"""Command-line interface for Weather CLI."""

import argparse
import sys
from typing import Optional, List

from . import __version__
from .config import Config
from .weather import WeatherClient


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="weather-cli",
        description="Fetch current weather information for any city",
        epilog="Example: weather-cli London"
    )

    parser.add_argument(
        "city",
        nargs="+",
        help="City name (can include spaces, e.g., 'New York')"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )

    parser.add_argument(
        "--units",
        choices=["metric", "imperial", "standard"],
        default="metric",
        help="Temperature units (default: metric/Celsius)"
    )

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main entry point for the CLI application.

    Args:
        argv: Command-line arguments (defaults to sys.argv).

    Returns:
        Exit code (0 for success, 1 for error).
    """
    parser = create_parser()
    args = parser.parse_args(argv)

    # Combine city name parts
    city = " ".join(args.city)

    # Initialize configuration
    config = Config()
    if args.units:
        config.units = args.units

    # Validate configuration
    if not config.validate():
        print(
            "Error: OPENWEATHER_API_KEY environment variable is not set.",
            file=sys.stderr
        )
        print(
            "\nPlease set your API key:",
            file=sys.stderr
        )
        print(
            "  export OPENWEATHER_API_KEY='your_api_key_here'",
            file=sys.stderr
        )
        print(
            "\nGet your free API key at: https://openweathermap.org/api",
            file=sys.stderr
        )
        return 1

    # Fetch and display weather
    try:
        with WeatherClient(config) as client:
            weather = client.get_weather(city)
            if weather:
                print(weather)
                return 0
            else:
                print("Failed to fetch weather data.", file=sys.stderr)
                return 1

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
