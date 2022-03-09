import pandas
data = pandas.read_csv("weather_data.csv")
data_list = data["temp"].to_list()

count = 0
number_of_temp = 0
for i in range(len(data_list)):
    count += data_list[i]
    number_of_temp = i

avg = round(count / number_of_temp, 2)
print(avg)

x = data["temp"].mean()
y = data["temp"].max()
print(y)

print(data.condition)

# Get data in a row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
fahrenhite = (monday.temp * 9/5) + 32
print(fahrenhite)

data_dict = {
    "students": ["Ervin", "Emel", "Ines"],
    "scores": [90, 91, 89],
}

to_csv = pandas.DataFrame(data_dict)
to_csv.to_csv("data_csv.csv")