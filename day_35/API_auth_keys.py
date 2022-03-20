# OpenWeather API key
import requests
from twilio.rest import Client

api_key = "your_api"
weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "your_sid"
auth_token = "your_auth"

params = {
    "lat": 51.759048,
    "lon": 19.458599,
    "appid": api_key,
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
        from_="number_choosen",
        to="your_verified_nuber"
        )
    print(message.status)


