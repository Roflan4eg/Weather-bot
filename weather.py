import requests
def get_weather(city,weather_token,lang='en'):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric&lang={lang}"
    try:
        r = requests.get(url)
        data = r.json()
        city_name = data["name"]
        temp = data["main"]["temp"]
        weather_status = data["weather"][0]["description"]
        feels_like = data["main"]["feels_like"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        humidity = data["main"]["temp_max"]
        wind_speed = data["wind"]["speed"]
        result = {"city_name": city_name, "temp": temp, "weather_status": weather_status,
                  "feels_like": feels_like, "temp_min":  temp_min, "temp_max": temp_max,
                  "humidity": humidity, "wind_speed": wind_speed}
        return result
    except:
        return 0