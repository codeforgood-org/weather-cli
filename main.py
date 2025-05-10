import requests
import sys

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        city_name = data['name']
        print(f"Weather in {city_name}: {weather}, {temp}°C")
    else:
        print("Error fetching weather data. Check city name or API key.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python weather.py [city]")
        return
    city = " ".join(sys.argv[1:])
    get_weather(city)

if __name__ == "__main__":
    main()
