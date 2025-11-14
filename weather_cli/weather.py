"""Weather data fetching and processing."""

from typing import Dict, Any, Optional
import requests

from .config import Config


class WeatherData:
    """Class to represent weather data."""

    def __init__(self, data: Dict[str, Any]):
        """
        Initialize weather data from API response.

        Args:
            data: JSON response from OpenWeatherMap API.
        """
        self.city = data.get("name", "Unknown")
        self.country = data.get("sys", {}).get("country", "")
        self.description = data.get("weather", [{}])[0].get("description", "N/A")
        self.temperature = data.get("main", {}).get("temp", 0)
        self.feels_like = data.get("main", {}).get("feels_like", 0)
        self.humidity = data.get("main", {}).get("humidity", 0)
        self.pressure = data.get("main", {}).get("pressure", 0)
        self.wind_speed = data.get("wind", {}).get("speed", 0)
        self.clouds = data.get("clouds", {}).get("all", 0)

    def __str__(self) -> str:
        """
        Format weather data as a string.

        Returns:
            str: Formatted weather information.
        """
        location = f"{self.city}, {self.country}" if self.country else self.city
        return f"""
Weather in {location}:
  Description: {self.description.capitalize()}
  Temperature: {self.temperature}°C (feels like {self.feels_like}°C)
  Humidity: {self.humidity}%
  Pressure: {self.pressure} hPa
  Wind Speed: {self.wind_speed} m/s
  Cloudiness: {self.clouds}%
"""


class WeatherClient:
    """Client for fetching weather data from OpenWeatherMap API."""

    def __init__(self, config: Config):
        """
        Initialize the weather client.

        Args:
            config: Configuration object containing API key and settings.
        """
        self.config = config
        self.session = requests.Session()

    def get_weather(self, city: str) -> Optional[WeatherData]:
        """
        Fetch weather data for a given city.

        Args:
            city: Name of the city to get weather for.

        Returns:
            WeatherData object if successful, None otherwise.

        Raises:
            ValueError: If city name is empty.
            requests.RequestException: If API request fails.
        """
        if not city or not city.strip():
            raise ValueError("City name cannot be empty")

        params = {
            "q": city.strip(),
            "appid": self.config.get_api_key(),
            "units": self.config.units
        }

        try:
            response = self.session.get(
                self.config.base_url,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return WeatherData(response.json())

        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                raise ValueError(f"City '{city}' not found") from e
            elif response.status_code == 401:
                raise ValueError("Invalid API key") from e
            else:
                raise requests.RequestException(
                    f"HTTP error occurred: {e}"
                ) from e

        except requests.exceptions.ConnectionError as e:
            raise requests.RequestException(
                "Connection error. Please check your internet connection."
            ) from e

        except requests.exceptions.Timeout as e:
            raise requests.RequestException(
                "Request timed out. Please try again."
            ) from e

        except requests.exceptions.RequestException as e:
            raise requests.RequestException(
                f"An error occurred while fetching weather data: {e}"
            ) from e

    def close(self):
        """Close the HTTP session."""
        self.session.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
