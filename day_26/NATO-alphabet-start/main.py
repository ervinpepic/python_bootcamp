import pandas


csv_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
letters_dict = {word.letter: word.code for (letter, word) in csv_dict.iterrows() }
game_on = True
while game_on:
    user_input = input("Your name? ")
    user_name = [name.capitalize() for name in user_input]
    phonetic_name = [word for letter,word in letters_dict.items() if letter in user_name]
    try:
        list_new = [letters_dict[letter] for letter in user_name]
    except KeyError:
        print("Sorry, please use only alphabetic input not numeric or symbols!")
    else:
        list_new = [letters_dict[letter] for letter in user_name]
        print(list_new)
        game_on = False
    

#This way 


# print(list_new)
