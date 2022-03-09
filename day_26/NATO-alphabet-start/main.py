import pandas


csv_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
letters_dict = {word.letter: word.code for (letter, word) in csv_dict.iterrows() }

user_input = input("Your name? ")
user_name = [name.capitalize() for name in user_input]
#This way 
phonetic_name = [word for letter,word in letters_dict.items() if letter in user_name]
#or this way
list_new = [letters_dict[letter] for letter in user_name]

print(list_new)
