print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int("How old are you? ")
    if age <=12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.")


# Day 3 Task 2:
"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

result = round(weight / (height ** 2))

if result < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif result > 18.5 and result < 25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif result > 25 and result < 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif result > 30 and result < 35:
    print(f"Your BMI is {result}, you are obese.")
else:
    print(f"Your BMI is {result},you are clinically obese.")




# Day 3 Task 3:

year = int(input("Which year do you want to check? "))

current_year = year * 365

if current_year % 4 == 0:
    print("Leap year.")
elif current_year % 100 != 0:
    print("Not leap year.")
elif current_year % 400 == 0:
    print("Leap year.")