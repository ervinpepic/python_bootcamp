print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int("How old are you? ")
    if age <=12:
        print("Please pay $5.")
        bill = 5
    elif age <=18:
        print("Please pay $7.")
        bill = 7
    elif age >=45 and age <=55:
        print("Have a free ride.")
    else:
        print("Please pay $12")
        bill = 12
    photo_inlucded = input("Want a photo? Y or N")
    if photo_inlucded == "Y":
        bill += 3
    print(f"Your bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

#Day 3 task 5:

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

count_1 = name1.lower().count('t') + name1.lower().count('r') + name1.lower().count('u') + name1.lower().count('e') + name2.lower().count('t') + name2.lower().count('r')  + name2.lower().count('u')  + name2.lower().count('e')

count_2 = name1.lower().count('l') + name1.lower().count('o') + name1.lower().count('v') + name1.lower().count('e') + name2.lower().count('l')  + name2.lower().count('o')  + name2.lower().count('v')  + name2.lower().count('e')

x = str(count_1)
y = str(count_2)
final = x + y

x = int(final)
if x < 10 or x > 90:
    print(f"Your score is {x}, you go together like coke and mentos.")
elif x >= 40 and x <=50:
    print(f"Your score is {x}, you are alright together.")
else:
    print(f"Your score is {x}.")

# another way

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

final_string = name1 + name2
lfs = final_string.lower()

t = lfs.count('t')
r = lfs.count('r')
u = lfs.count('u')
e = lfs.count('e')

true = t + r + u + e

l = lfs.count('l')
o = lfs.count('o')
v = lfs.count('v')
e = lfs.count('e')

love = l + o + v + e

ls = str(true) + str(love)
love_score = int(ls)
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40 and love_score <=50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

