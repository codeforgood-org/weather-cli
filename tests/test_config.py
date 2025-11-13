"""Tests for config module."""

import os
import pytest
from weather_cli.config import Config


class TestConfig:
    """Test cases for Config class."""

    def test_config_initialization(self, monkeypatch):
        """Test that config initializes correctly."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_api_key")
        config = Config()
        assert config.api_key == "test_api_key"
        assert config.base_url == "https://api.openweathermap.org/data/2.5/weather"
        assert config.units == "metric"

    def test_config_custom_units(self, monkeypatch):
        """Test that custom units can be set."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_api_key")
        monkeypatch.setenv("WEATHER_UNITS", "imperial")
        config = Config()
        assert config.units == "imperial"

    def test_validate_with_api_key(self, monkeypatch):
        """Test validation passes with API key."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_api_key")
        config = Config()
        assert config.validate() is True

    def test_validate_without_api_key(self, monkeypatch):
        """Test validation fails without API key."""
        monkeypatch.delenv("OPENWEATHER_API_KEY", raising=False)
        config = Config()
        assert config.validate() is False

    def test_get_api_key_success(self, monkeypatch):
        """Test getting API key when it exists."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_api_key")
        config = Config()
        assert config.get_api_key() == "test_api_key"

    def test_get_api_key_failure(self, monkeypatch):
        """Test getting API key raises error when not set."""
        monkeypatch.delenv("OPENWEATHER_API_KEY", raising=False)
        config = Config()
        with pytest.raises(ValueError, match="API key not found"):
            config.get_api_key()
