def transform(weather_json: dict):
    return {
        "city": weather_json["name"],
        "temperature": weather_json["main"]["temp"],
        "humidity": weather_json["main"]["humidity"],
        "pressure": weather_json["main"]["pressure"],
        "wind_speed": weather_json["wind"]["speed"],
        "weather_description": weather_json["weather"][0]["description"]
    }
