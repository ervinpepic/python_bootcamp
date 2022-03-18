from time import sleep
from requests import request
from datetime import datetime
import smtplib


my_email = "myemail@email"
my_password = "mypass"

LAT = 42.841400
LNG = 20.165291


def is_near_me():
    response = request.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if LAT - 5 <= iss_latitude <= LAT + 5 and LNG - 5 <= iss_longitude <= LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": LAT,
        "lng": LNG,
        "formatted": 0,
    }

    response = request.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    sleep(60)
    if is_near_me() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                    from_addr=my_email, 
                    to_addrs="receiver_email@mail", 
                    msg=f"Subject:Look at the sky\n\n Now iss is over your sky"
            )