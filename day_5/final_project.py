#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_generator = []
final_pass = ""

for letter in range(0, nr_letters + 1):
    # letters_array.append(letters[letter])
    password_generator.append(random.choice(letters))
# random.shuffle(password_generator)

for symbol in range(0, nr_symbols + 1):
    # symbols_array.append(symbols[symbol])
    password_generator.append(random.choice(symbols))
# random.shuffle(symbols_array)

for number in range(0, nr_numbers + 1):
    # numbers_array.append(numbers[number])
    password_generator.append(random.choice(numbers))
# random.shuffle(numbers_array)

# password_generator = [letters_array, symbols_array, numbers_array]
random.shuffle(password_generator)

for password in password_generator:
    final_pass += password
print(final_pass)

# for password_combination in password_generator:
#     for password in password_combination:
#         print(password, end='')
#     print    


