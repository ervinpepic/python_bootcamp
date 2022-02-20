# def greet():
#     print("Hello, ")
#     print("World, ")
#     print("Bye...")

# greet()

# def greet_dynamic(name):
#     print(f"Hello {name}!")
#     print(f"Here is what is new today, {name} ")
#     print(f"Bye...{name}")

# greet_dynamic("Ervin")


# # Functions with more than 1 input

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is weather today in the {location}")

# greet_with(name="Ervin", location="Rozaje")

# Day 8, task 1
# def paint_calc(height, width, cover):
#     x = (height * width) / cover
#     e = int(math.ceil(x))
#     print(f"You'll need {e} cans of paint.")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# paint_calc(height=test_h, width=test_w, cover=coverage)


def prime_checker(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(f"It's not a prime number.")
                break
        else:
            print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)