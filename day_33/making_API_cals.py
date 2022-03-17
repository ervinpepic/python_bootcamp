import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

lng = data["iss_position"]["longitude"]
ltd = data["iss_position"]["latitude"]

iss_position = (lng, ltd)

print(iss_position)