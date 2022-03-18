from urllib import response
import requests
from datetime import datetime
LAT = 42.841400
LNG = 20.165291

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunset, sunrise)
time_now = datetime.now().hour
print(time_now)