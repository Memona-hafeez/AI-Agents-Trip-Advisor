import requests
import random
from datetime import datetime

# Static lat/lon for major Pakistani cities
city_coords = {
    "lahore": (31.5497, 74.3436),
    "islamabad": (33.6844, 73.0479),
    "karachi": (24.8607, 67.0011),
    "swat": (35.2180, 72.4258),
    "gilgit": (35.9221, 74.3087),
    "quetta": (30.1798, 66.9750),
    "murree": (33.9062, 73.3916)
}

# Mock weather data as fallback
mock_weather_data = {
    "lahore": {"temp": 35, "weather": "Sunny", "wind": 12},
    "islamabad": {"temp": 28, "weather": "Partly Cloudy", "wind": 8},
    "karachi": {"temp": 32, "weather": "Humid", "wind": 15},
    "swat": {"temp": 22, "weather": "Cool", "wind": 5},
    "gilgit": {"temp": 18, "weather": "Cold", "wind": 10},
    "quetta": {"temp": 25, "weather": "Dry", "wind": 20},
    "murree": {"temp": 20, "weather": "Misty", "wind": 6}
}

def get_weather_and_safety(city):
    city_key = city.lower()
    if city_key not in city_coords:
        return f"❌ City '{city}' not supported."
    
    lat, lon = city_coords[city_key]
    current_weather = {}
    api_success = False

    # Try Open-Meteo API with increased timeout and better error handling
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        # Increased timeout to 20 seconds
        weather_resp = requests.get(weather_url, timeout=20)
        if weather_resp.status_code == 200:
            weather_data = weather_resp.json()
            current_weather = weather_data.get("current_weather", {})
            api_success = True
        else:
            raise Exception(f"API returned status code: {weather_resp.status_code}")
    except requests.exceptions.Timeout:
        print("⚠️ Weather API timeout - using fallback data")
    except requests.exceptions.ConnectionError:
        print("⚠️ Weather API connection failed - using fallback data")
    except Exception as e:
        print(f"⚠️ Weather API error: {e} - using fallback data")

    # Use mock data if API fails
    if not api_success and city_key in mock_weather_data:
        mock_data = mock_weather_data[city_key]
        current_weather = {
            "temperature": mock_data["temp"],
            "weathercode": mock_data["weather"],
            "windspeed": mock_data["wind"]
        }

    # REST Countries API for Pakistan (with better error handling)
    region = "N/A"
    population = "N/A"
    try:
        country_url = "https://restcountries.com/v3.1/name/pakistan"
        country_resp = requests.get(country_url, timeout=15)
        if country_resp.status_code == 200:
            country_data = country_resp.json()
            region = country_data[0].get("region", "N/A")
            population = country_data[0].get("population", "N/A")
    except Exception as e:
        print(f"⚠️ Country API error: {e}")

    # Enhanced safety tips based on city
    safety_tips = {
        "lahore": "Be cautious in crowded areas. Keep valuables secure. Respect local customs.",
        "islamabad": "Generally safe city. Follow traffic rules. Be respectful of government areas.",
        "karachi": "Exercise caution in certain areas. Avoid isolated places at night.",
        "swat": "Beautiful but remote. Travel with local guides. Check weather conditions.",
        "gilgit": "High altitude area. Acclimatize properly. Carry warm clothing.",
        "quetta": "Be aware of weather changes. Follow local advice for travel.",
        "murree": "Tourist-friendly hill station. Drive carefully on winding roads."
    }
    
    safety_tip = safety_tips.get(city_key, "Exercise usual safety precautions. Respect local customs.")

    return {
        "City": city.title(),
        "Temperature (C)": current_weather.get("temperature", "N/A"),
        "Weather": current_weather.get("weathercode", "N/A"),
        "Wind Speed (km/h)": current_weather.get("windspeed", "N/A"),
        "Region": region,
        "Population": population,
        "Safety Tip": safety_tip,
        "Data Source": "Live API" if api_success else "Fallback Data"
    }

if __name__ == "__main__":
    city = input("Enter a Pakistani city (e.g., Lahore, Islamabad, Karachi): ")
    result = get_weather_and_safety(city)
    if isinstance(result, dict):
        print(f"\nWeather & Safety for {result['City']}:")
        print(f"Temperature: {result['Temperature (C)']}°C")
        print(f"Weather: {result['Weather']}")
        print(f"Wind Speed: {result['Wind Speed (km/h)']} km/h")
        print(f"Region: {result['Region']}")
        print(f"Population: {result['Population']}")
        print(f"Safety Tip: {result['Safety Tip']}")
        print(f"Data Source: {result['Data Source']}")
    else:
        print(result) 