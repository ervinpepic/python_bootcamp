import os
import requests
import lxml
import smtplib

from email import message
from bs4 import BeautifulSoup

email_ = os.environ.get("EMAIL")
pass_ = os.environ.get("PASSWORD")


PRODUCT_URL = os.environ.get("PRODUCT_URL")

headers = {
    "Accept-Language": "en-US,en;q=0.9,hr;q=0.8,sr;q=0.7,de;q=0.6,sl;q=0.5,bs;q=0.4",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}

response = requests.get(url=PRODUCT_URL, headers=headers)
html = response.text

soup = BeautifulSoup(html, "lxml")

price_tag = soup.find(name="span", class_="a-offscreen")
product_price = float(price_tag.getText().split("$")[1])

title_tag = soup.find(name="span", id="productTitle")
product_title = title_tag.getText().strip()
message = f"Hello there, the product {product_title} is now on sale with price of ${product_price}. \nCheck it on this link {PRODUCT_URL}"
if 200 < product_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_, password=pass_)
        connection.sendmail(
            from_addr=email_,
            to_addrs="pepic_ervin@hotmail.com",
            msg=f"Subject:AMAZON PRODUCT SALE\n\n{message}"
        )