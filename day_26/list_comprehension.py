# without list comprehension the old way

numbers = [1 , 2, 3]
new_list = []

for n in numbers:
    add1 = n + 1
    new_list.append(add1)

# same aproach with list comprehension

new_list_1 = [n + 1 for n in numbers]
print(new_list_1)

name = "Ervin"
capitalised = [letter.capitalize() for letter in name]
print(capitalised)
x = range(1, 5)
new_range = [multiply * 2 for multiply in x]
print(new_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) == 4]
print(short_names)

capitalised_names = [name.upper() for name in names if len(name) > 5]
print(capitalised_names)

#day 26 task 1


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [number * number for number in numbers]
print(squared_numbers)


#day 26 task 2
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

#day 26 task 2