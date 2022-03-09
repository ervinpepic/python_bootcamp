import pandas

data = pandas.read_csv("squirel.csv")
# x = data["Primary Fur Color"].value_counts()
# y = x.tolist()
# gray = y[0]
# red = y[1]
# black = y[2]
# squirel_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [gray, red, black]
# }
# t = pandas.DataFrame(squirel_dict)
# t.to_csv("s.csv")

#or 

gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
squirel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, red, black]
}
t = pandas.DataFrame(squirel_dict)
t.to_csv("s.csv")