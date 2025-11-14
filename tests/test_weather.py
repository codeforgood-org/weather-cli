"""Tests for weather module."""

import pytest
import responses
from requests.exceptions import RequestException

from weather_cli.config import Config
from weather_cli.weather import WeatherClient, WeatherData


class TestWeatherData:
    """Test cases for WeatherData class."""

    def test_weather_data_initialization(self):
        """Test WeatherData initialization with API response."""
        data = {
            "name": "London",
            "sys": {"country": "GB"},
            "weather": [{"description": "clear sky"}],
            "main": {
                "temp": 20.5,
                "feels_like": 19.8,
                "humidity": 65,
                "pressure": 1015
            },
            "wind": {"speed": 3.5},
            "clouds": {"all": 10}
        }
        weather = WeatherData(data)

        assert weather.city == "London"
        assert weather.country == "GB"
        assert weather.description == "clear sky"
        assert weather.temperature == 20.5
        assert weather.feels_like == 19.8
        assert weather.humidity == 65
        assert weather.pressure == 1015
        assert weather.wind_speed == 3.5
        assert weather.clouds == 10

    def test_weather_data_string_representation(self):
        """Test string representation of WeatherData."""
        data = {
            "name": "Tokyo",
            "sys": {"country": "JP"},
            "weather": [{"description": "cloudy"}],
            "main": {"temp": 25, "feels_like": 24, "humidity": 70, "pressure": 1010},
            "wind": {"speed": 5},
            "clouds": {"all": 50}
        }
        weather = WeatherData(data)
        result = str(weather)

        assert "Tokyo, JP" in result
        assert "Cloudy" in result  # Should be capitalized
        assert "25°C" in result
        assert "70%" in result


class TestWeatherClient:
    """Test cases for WeatherClient class."""

    def test_client_initialization(self, monkeypatch):
        """Test WeatherClient initialization."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_key")
        config = Config()
        client = WeatherClient(config)
        assert client.config == config

    @responses.activate
    def test_get_weather_success(self, monkeypatch):
        """Test successful weather fetch."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_key")

        # Mock API response
        responses.add(
            responses.GET,
            "https://api.openweathermap.org/data/2.5/weather",
            json={
                "name": "Paris",
                "sys": {"country": "FR"},
                "weather": [{"description": "sunny"}],
                "main": {"temp": 22, "feels_like": 21, "humidity": 60, "pressure": 1013},
                "wind": {"speed": 2.5},
                "clouds": {"all": 20}
            },
            status=200
        )

        config = Config()
        client = WeatherClient(config)
        weather = client.get_weather("Paris")

        assert weather is not None
        assert weather.city == "Paris"
        assert weather.country == "FR"
        assert weather.temperature == 22

    def test_get_weather_empty_city(self, monkeypatch):
        """Test that empty city name raises ValueError."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_key")
        config = Config()
        client = WeatherClient(config)

        with pytest.raises(ValueError, match="City name cannot be empty"):
            client.get_weather("")

    @responses.activate
    def test_get_weather_city_not_found(self, monkeypatch):
        """Test handling of 404 error."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_key")

        responses.add(
            responses.GET,
            "https://api.openweathermap.org/data/2.5/weather",
            json={"message": "city not found"},
            status=404
        )

        config = Config()
        client = WeatherClient(config)

        with pytest.raises(ValueError, match="City .* not found"):
            client.get_weather("InvalidCity123")

    @responses.activate
    def test_get_weather_invalid_api_key(self, monkeypatch):
        """Test handling of 401 error."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "invalid_key")

        responses.add(
            responses.GET,
            "https://api.openweathermap.org/data/2.5/weather",
            json={"message": "Invalid API key"},
            status=401
        )

        config = Config()
        client = WeatherClient(config)

        with pytest.raises(ValueError, match="Invalid API key"):
            client.get_weather("London")

    def test_context_manager(self, monkeypatch):
        """Test that client works as context manager."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_key")
        config = Config()

        with WeatherClient(config) as client:
            assert client is not None
            assert client.session is not None
