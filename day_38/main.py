import os
import requests
from datetime import datetime

time = datetime.now()
date_now = time.strftime("%d/%m/%Y")
time_now = time.strftime("%H:%M:%S")

NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONX_KEY = os.environ.get("NUTRITIONX_KEY")
NUTRITIONX_APP_ID = os.environ.get("NUTRITIONX_APP_ID")

SHEETY_ENDOPINT = os.environ.get("SHEETY_ENDOPINT")


nutrition_headers = {
    "x-app-id": NUTRITIONX_APP_ID,
    "x-app-key": NUTRITIONX_KEY,
    "Content-Type": "application/json"
}

nutrition_dict = {
    "query": input("Describe what activities do you have today? => ")
}

response = requests.post(url=NUTRITION_ENDPOINT, json=nutrition_dict, headers=nutrition_headers)
data = response.json()


calories = data["exercises"][0]["nf_calories"]
duration = data["exercises"][0]["duration_min"]
exercise = data["exercises"][0]["name"].title()

sheety_dict = {
    "workout": {
        "date": date_now,
        "time": time_now,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

sheety_headers = {
    "Authorization": f"Bearer {os.environ.get('AUTH_TOKEN')}"
}

sheety_response = requests.post(url=SHEETY_ENDOPINT, json=sheety_dict, headers=sheety_headers)

print(os.environ.get('AUTH_TOKEN'))