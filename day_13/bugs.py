# describe the problem

def my_function_with_bug():
    for i in range(1, 20):
        if i == 20:
            print("Finished, that's it.")

def my_function_without_bug():
    for i in range(1, 21):
        if i == 20:
            print("Finished, that's it.")

my_function_with_bug()
my_function_without_bug()

from random import randint
dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

year = int(input("What's your year of birth? "))
if year >= 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

age = int(input("How old are you? "))
if age > 18:
    print(f"You cam drive at age {age}")

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

def mutate(a_list):
    b_list = []
    for i in a_list:
        new_i = i * 2
        b_list.append(new_i)
    print(b_list)
mutate([1, 2, 3, 4, 5, 6, 12, 18])