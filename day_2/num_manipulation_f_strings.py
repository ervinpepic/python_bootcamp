a = round(8 / 3, 5)
print(a)
x = 8 // 3
x /= 2 #take the previous sum and divide it by 2
print(x)
# flor division //

# F strings using for mixing strings and numbers together or insert number inside strings

x = 10
y = 1
print(f"x is equal to: {x} and y is {y}")

# task 3 day 2

age = int(input("What is your current age? "))
final_age = 90

days = (final_age * 365) - (age * 365) 
weeks = (final_age * 52) - (age * 52) 
months = (final_age * 12) - (age * 12) 

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

