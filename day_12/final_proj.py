import random
from xmlrpc.client import boolean
# from art import logo
# print(logo)
print('Welcome to the Number Guessing game \n')

computer_number = random.randint(1, 100)
print("I'm thinking about one number between 1 and 100!")

choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def guess_checker(user, pc):
    global game_end
    if user > pc:
        print("Too high")
    if user < pc:
        print("Too low")
    if user == pc:
        print("You guess it! Congrats \n End of the Game!")
        game_end = True
        return game_end

game_end = False
easy = 10
hard = 5

while not game_end:
    user_number = int(input("Enter your guess: => "))

    if choose_level == "easy":
        guess_checker(user_number, computer_number)
        easy -= 1
        if not game_end:
            print(f"You have {easy} try left")
        if easy == 0:
            game_end = True

    elif choose_level == "hard":
        guess_checker(user_number, computer_number)
        hard -= 1
        if not game_end:
            print(f"You have {hard} try left")
        if hard == 0:
            print("You lose :(. No guess")
            game_end = True
    else:
        print("Invalid arguments")


    # if level == "easy":
    #     if user_number > computer_number:
    #         easy -= 1
    #         print("Too high")
    #         print(f"You have {easy} try left")
    #     elif user_number < computer_number:
    #         easy -= 1
    #         print("Too low")
    #         print(f"You have {easy} try left")
    #     if easy == 0:
    #         game_end = True
    #         print("No guess. Game over")
    #     if user_number == computer_number:
    #         print("You guess it!")
    #         game_end = True
    # if level == "hard":
    #     if user_number > computer_number:
    #         hard -= 1
    #         print("Too high")
    #         print(f"You have {hard} try left")
    #     elif user_number < computer_number:
    #         hard -= 1
    #         print("Too low")
    #         print(f"You have {hard} try left")
    #     if hard == 0:
    #         game_end = True
    #         print("No guess. Game over")
    #     if user_number == computer_number:
    #         print("You guess it! Congrats!")
    #         game_end = True
