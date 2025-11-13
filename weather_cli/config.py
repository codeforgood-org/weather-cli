"""Configuration management for Weather CLI."""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


class Config:
    """Configuration class for managing API keys and settings."""

    def __init__(self):
        """Initialize configuration from environment variables."""
        self.api_key: Optional[str] = os.getenv("OPENWEATHER_API_KEY")
        self.base_url: str = "https://api.openweathermap.org/data/2.5/weather"
        self.units: str = os.getenv("WEATHER_UNITS", "metric")

    def validate(self) -> bool:
        """
        Validate that required configuration is present.

        Returns:
            bool: True if configuration is valid, False otherwise.
        """
        return self.api_key is not None and self.api_key != ""

    def get_api_key(self) -> str:
        """
        Get the API key.

        Returns:
            str: The OpenWeatherMap API key.

        Raises:
            ValueError: If API key is not configured.
        """
        if not self.api_key:
            raise ValueError(
                "API key not found. Please set the OPENWEATHER_API_KEY "
                "environment variable."
            )
        return self.api_key
