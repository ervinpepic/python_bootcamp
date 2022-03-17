from datetime import datetime
import random
import smtplib

my_email = "myemail@email"
my_password = "mypass"

with open("quotes.txt", 'r') as file:
    content = file.readlines()
    message = random.choice(content)

today = datetime.now()
weekday = datetime.weekday(today)
if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
                from_addr=my_email, 
                to_addrs="mail@mail", 
                msg=f"Subject:Motivational email for this Monday\n\n{message}"
        )