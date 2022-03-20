# OpenWeather API key
import requests
import os
from twilio.rest import Client

# Open Weather
open_weather_api_key = os.environ.get("WEATHER_API_KEY")
weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# Twilio
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

params = {
    "lat": 51.759048,
    "lon": 19.458599,
    "appid": open_weather_api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=weather_endpoint, params=params)
response.raise_for_status()

weather_data = response.json()
weather_for_12_days = weather_data["hourly"][:12]
rain = False

for weather_id_code in weather_for_12_days:
    w_c = weather_id_code["weather"][0]["id"]
    if int(w_c) > 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring un umbrella! It will be rainy...", 
        from_=os.environ.get("TWILIO_FROM_NUMBER"),
        to=os.environ.get("TWILIO_TO_NUMBER")
        )
    print(message.status)


