print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

#(12 / 142) * 100

percentage_from_total_bill = total_bill * tip_percentage / 100
result = total_bill + percentage_from_total_bill / number_of_people
#result = "{:.2f}".format()
print(f"Each person shoyld pay: ${round(result, 2)}")