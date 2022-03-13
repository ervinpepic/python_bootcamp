# Try to openin file that doesn't exist without try: catch: blocks

# Output FileNotFoundError
with open("my_file.txt") as file_open:
    file_open.read()

# KeyError
my_dict = {"key": "value"}
value = my_dict["my_key"]

# IndexError
fruit_list = ["Jabuka", "Banana", "Breskva"]
fruid = fruit_list[4]

# TypeError
text = "abc"
print(text + 5)

# Try to openin file that doesn't exist with try: catch: blocks
try:
    file = open("my_file.txt")
    my_dict = {"key": "value"}
    print(my_dict["ervin"])
except FileNotFoundError:
    file = open("my_file.txt", 'w')
    file.write("My text\n")
except KeyError as error_message:
    print(f"Nema kljuca {error_message} koji pokusavate da indexirate!")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("Closed file to clean up memoru addresses!")

# Make your own exceptions

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height sholud not be over 3 meters!")
bmi = weight / height ** 2
print(bmi)

# Day 30 task 1
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

# Day 30 task 2

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)
