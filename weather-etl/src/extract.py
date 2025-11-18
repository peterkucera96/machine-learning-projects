import requests
import json

def get_weather(api_key: str, city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API request failed: {response.text}")

    return response.json()
