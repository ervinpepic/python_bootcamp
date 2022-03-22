from datetime import datetime
import json
import os
import re
import requests
date_now = datetime.now()
today_date = date_now.strftime("%Y%m%d")
print(today_date)


AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
USERNAME = "pepicervin"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

user_params = {
    "token": AUTH_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": AUTH_TOKEN
}
# response = requests.post(url=GRAPH_ENDPOINT,json=graph_params, headers=headers)
# print(response.text)

CREATE_GRAPH_ENDPOINT= f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_params['id']}"

create_graph_params = {
    "date": today_date,
    "quantity": input("How many minutes you are worked today? ")
}
response = requests.post(url=CREATE_GRAPH_ENDPOINT, json=create_graph_params, headers=headers)

print(response.text)

update_graph_params = {
    "quantity": "59.2",
    "optionalData": "{\"Day_37\":\"Update Finished\"}"
}

UPDATE_DELETE_GRAPH_PIXEL_ENDPOINT = f"{CREATE_GRAPH_ENDPOINT}/{today_date}"
# response = requests.put(url=UPDATE_GRAPH_PIXEL_ENDPOINT, json=update_graph_params, headers=headers)
response = requests.delete(url=UPDATE_DELETE_GRAPH_PIXEL_ENDPOINT, headers=headers)
print(response.text)

