import os
import math
import requests
from datetime import datetime
from time import strftime

from twilio.rest import Client


yesterday = datetime.now().day - 1
day_bf_yesterday = datetime.now().day - 4
ys_date = strftime(f"%Y-%m-%{yesterday}")
dbf_ys_date = strftime(f"%Y-%m-%{day_bf_yesterday}")


STOCK_NAME = "TSLA"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK_ENDPOINT = os.environ.get("STOCK_ENDPOINT")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

stock_array = [stock for (day, stock) in stock_data.items()]
yesterday_stock = float(stock_array[0]["4. close"])
dbf_yesterday_stock = float(stock_array[1]["4. close"])

diff = abs(yesterday_stock - dbf_yesterday_stock)
increase_decrease = math.floor((diff / yesterday_stock) * 100)

stock_status = None
if diff > 0:
    stock_status = "🔺"
else:
    stock_status = "🔻"


COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_ENDPOINT = os.environ.get("NEWS_ENDPOINT")


TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
TWILIO_AUTH_NUM = os.environ.get("TWILIO_AUTH_NUM")


news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

if abs(increase_decrease) >= 1:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    news_articles = news_data[:3]
    to_send_articles = [
        f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_articles]

    for article in to_send_articles:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f"{STOCK_NAME} {stock_status} {article}",
            from_=TWILIO_NUMBER,
            to=TWILIO_AUTH_NUM
        )
        print(message.status)
