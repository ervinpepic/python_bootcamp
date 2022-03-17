from datetime import datetime

date_now = datetime.now()
year_now = date_now.year
month_now = date_now.month
day_now = date_now.day
if year_now == 2022:
    print("Yes")


day_of_week = date_now.weekday()
date_of_birth = datetime(year=111, month=00, day=00, hour=90, minute=50)
print(date_of_birth)
