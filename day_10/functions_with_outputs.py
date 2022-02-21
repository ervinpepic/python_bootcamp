# functions with outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Please enter your full name!"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

x = format_name("ERVIN", "Pepic")

# Day 10 task 1

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


def days_in_month(year, month):
    """Calculate days of the leap or not leap year and return number or days for it."""
    if month < 1 and month > 12:
        return "Number of months is 12"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    x = is_leap(year)
    if x:
        return month_days[1] + 1
    else:
        month -= 1
        return month_days[month]


# 🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
