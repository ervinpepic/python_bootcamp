import os
import requests

SHEETY_GET_ENDPOINT = ""


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_GET_ENDPOINT)
        destination_data = response.json()["prices"]
        return destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            config_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_GET_ENDPOINT}/{city['id']}", json=config_data)
            print(response.text)
