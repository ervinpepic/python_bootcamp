import random
from xmlrpc.client import boolean
from art import logo

EASY = 10
HARD = 5

def guess_checker(user, pc, tryes):
    if user > pc:
        print("Too high")
        return tryes - 1
    if user < pc:
        print("Too low")
        return tryes - 1
    if user == pc:
        print("You guess it! Congrats \n End of the Game!")

def answer_check():
    choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choose_level == "easy":
        return EASY
    elif choose_level == "hard":
        return HARD

def gameplay(): 
    print(logo)
    print('Welcome to the Number Guessing game \n')
    print("I'm thinking about one number between 1 and 100!")

    computer_number = random.randint(1, 100)
    trying = answer_check()
    user_number = 0

    while user_number != computer_number:
        print(f"You have a {trying} times to guess the number")
        user_number = int(input("Guess a number => "))

        trying = guess_checker(user_number, computer_number, trying)
        if trying == 0:
            print("You don't guess a number. Game over!")
            return
        elif user_number != computer_number:
            print("Guess again")
gameplay()