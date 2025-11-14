"""Tests for CLI module."""

import pytest
import responses
from weather_cli.cli import create_parser, main


class TestCLI:
    """Test cases for CLI functionality."""

    def test_create_parser(self):
        """Test argument parser creation."""
        parser = create_parser()
        assert parser.prog == "weather-cli"

    def test_parser_city_argument(self):
        """Test parsing city argument."""
        parser = create_parser()
        args = parser.parse_args(["London"])
        assert args.city == ["London"]

    def test_parser_multi_word_city(self):
        """Test parsing multi-word city names."""
        parser = create_parser()
        args = parser.parse_args(["New", "York"])
        assert args.city == ["New", "York"]

    def test_parser_units_argument(self):
        """Test parsing units argument."""
        parser = create_parser()
        args = parser.parse_args(["Tokyo", "--units", "imperial"])
        assert args.units == "imperial"

    def test_parser_default_units(self):
        """Test default units."""
        parser = create_parser()
        args = parser.parse_args(["Tokyo"])
        assert args.units == "metric"

    def test_main_no_api_key(self, monkeypatch, capsys):
        """Test main function without API key."""
        monkeypatch.delenv("OPENWEATHER_API_KEY", raising=False)
        exit_code = main(["London"])
        captured = capsys.readouterr()

        assert exit_code == 1
        assert "OPENWEATHER_API_KEY" in captured.err

    @responses.activate
    def test_main_success(self, monkeypatch, capsys):
        """Test successful execution of main."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_key")

        responses.add(
            responses.GET,
            "https://api.openweathermap.org/data/2.5/weather",
            json={
                "name": "Berlin",
                "sys": {"country": "DE"},
                "weather": [{"description": "rainy"}],
                "main": {"temp": 15, "feels_like": 14, "humidity": 80, "pressure": 1008},
                "wind": {"speed": 4.5},
                "clouds": {"all": 90}
            },
            status=200
        )

        exit_code = main(["Berlin"])
        captured = capsys.readouterr()

        assert exit_code == 0
        assert "Berlin" in captured.out
        assert "15°C" in captured.out

    @responses.activate
    def test_main_city_not_found(self, monkeypatch, capsys):
        """Test main function with invalid city."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_key")

        responses.add(
            responses.GET,
            "https://api.openweathermap.org/data/2.5/weather",
            json={"message": "city not found"},
            status=404
        )

        exit_code = main(["InvalidCity123"])
        captured = capsys.readouterr()

        assert exit_code == 1
        assert "Error" in captured.err

    @responses.activate
    def test_main_with_units(self, monkeypatch, capsys):
        """Test main function with custom units."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "test_key")

        responses.add(
            responses.GET,
            "https://api.openweathermap.org/data/2.5/weather",
            json={
                "name": "Miami",
                "sys": {"country": "US"},
                "weather": [{"description": "hot"}],
                "main": {"temp": 85, "feels_like": 88, "humidity": 75, "pressure": 1012},
                "wind": {"speed": 10},
                "clouds": {"all": 30}
            },
            status=200
        )

        exit_code = main(["Miami", "--units", "imperial"])
        captured = capsys.readouterr()

        assert exit_code == 0
        assert "Miami" in captured.out
