from datetime import datetime
import pandas
import random
import smtplib

letters = [
    "./letter_templates/letter_1.txt", 
    "./letter_templates/letter_2.txt", 
    "./letter_templates/letter_3.txt"
]

my_email = "myemail@email"
my_password = "mypass"

now_date = datetime.now()
today_day = now_date.day
today_month = now_date.month
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(d["month"], d["day"]): d for (_, d) in data.iterrows()}
party_guy = birthdays_dict[today]
receiver_name = party_guy["name"]

if today in birthdays_dict:
    with open(random.choice(letters), 'r') as file:
        content = file.read()
        message = content.replace("[NAME]", receiver_name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
                from_addr=my_email, 
                to_addrs="receiver_email@mail", 
                msg=f"Subject:Happy birthday\n\n{message}"
        )
    