# OpenWeather API key
import requests
from twilio.rest import Client

api_key = "26a0e9d734bfd8221e9ac4963dec5c72"
weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC31e5dc9007cd12574bc6a1905ae2a514"
auth_token = "c55a0fce23364e86d1d56b4a93f8254d"

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


