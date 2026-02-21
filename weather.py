import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass
from typing import Optional, Tuple

# -------------------- CONFIG -------------------- #
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"
BASE_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


# -------------------- DATA MODEL -------------------- #
@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float


# -------------------- SERVICE LAYER -------------------- #
def get_lat_lon(city_name: str, state_code: str, country_code: str) -> Tuple[Optional[float], Optional[float]]:
    """
    Fetch latitude and longitude using OpenWeather Geocoding API
    """
    try:
        response = requests.get(
            BASE_GEO_URL,
            params={
                "q": f"{city_name},{state_code},{country_code}",
                "limit": 1,
                "appid": API_KEY
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        if not data:
            return None, None

        return data[0]["lat"], data[0]["lon"]

    except requests.RequestException as e:
        print(f"Geo API Error: {e}")
        return None, None


def get_current_weather(lat: float, lon: float) -> Optional[WeatherData]:
    """
    Fetch current weather using lat & lon
    """
    try:
        response = requests.get(
            BASE_WEATHER_URL,
            params={
                "lat": lat,
                "lon": lon,
                "appid": API_KEY,
                "units": "metric"
            },
            timeout=10
        )
        response.raise_for_status()
        resp = response.json()

        if not resp.get("weather") or not resp.get("main"):
            return None

        return WeatherData(
            main=resp["weather"][0]["main"],
            description=resp["weather"][0]["description"],
            icon=resp["weather"][0]["icon"],
            temperature=resp["main"]["temp"],
        )

    except requests.RequestException as e:
        print(f"Weather API Error: {e}")
        return None


# -------------------- BUSINESS LOGIC -------------------- #
def get_weather(city_name: str, state_code: str, country_code: str) -> Optional[WeatherData]:
    lat, lon = get_lat_lon(city_name, state_code, country_code)

    if lat is None or lon is None:
        print("City not found.")
        return None

    return get_current_weather(lat, lon)


# -------------------- RUNNER -------------------- #
if __name__ == "__main__":
    weather = get_weather("Ahmedabad", "GJ", "IN")

    if weather:
        print(weather)
    else:
        print("Unable to fetch weather.")