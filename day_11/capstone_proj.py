import os
import random
from art import logo

def deal_card():
    """ Take cards list and randomly choose one from the list and then return that value"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deal = random.choice(cards)
    return deal

def calculate_score(cards_list):
    """ Takes the List as the input, find if user or computer has a blackjack and check for the ACE. Return value is the sum of the List"""
    saldo = sum(cards_list)
    if 11 in cards_list and 10 in cards_list and len(cards_list) == 2:
        return 0
    if 11 in cards_list and saldo > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return saldo

def compare(user_score, pc_score):
    "Compare user and pc scores and return the winner"
    if user_score == pc_score:
        return "DRAW!"
    elif pc_score == 21:
        return "YOU LOSE :("
    elif user_score == 21:
        return "YOU WIN :)"
    elif user_score > 21:
        return "YOU LOSE :("
    elif pc_score > 21:
        return "YOU WIN :)"
    elif user_score > pc_score:
        return "YOU WIN :)"
    elif pc_score > user_score:
        return "YOU LOSE"

def game_play():
    """ This is the Recursive function. It will call itself when the user needs to play game again"""
    print(logo) #Show the logo on the start of the game.

    user_cards = [] # Created empty list for user deck
    computer_cards = [] # Created empty list for pc deck
    game_end = False # Boolean variable to test 

    for _ in range(2): # Foor loop get over deal_card function and add random number to the user and pc lists 2 times
        user_cards.append(deal_card()) # Adding 2 random number to the user list
        computer_cards.append(deal_card()) # Adding 2 random number to the pc list 

    while not game_end: # until the game_end variable goes True this while loop will iterate over again and again

        user_result = calculate_score(user_cards) # Adding calcuate_score function values to the user_result variable
        pc_result = calculate_score(computer_cards) # Adding calcuate_score function values to the pc variable

        print(f"Your cards: {user_cards}, current score: {user_result}") #print results to the screen
        print(f"Computer cards: [{computer_cards[0]}, X] , current score: {pc_result}")

        if user_result == 0 or pc_result == 0 or user_result > 21: #Cheking for the truthines of the game rules
            game_end = True
            print("Game over!")
        else:
            user_another_try = input("Do you want to do another try? 'y' for try again 'n' for end: => ").lower()

            if user_another_try == "y":
                user_cards.append(deal_card())
            else:
                game_end = True
                print("Game over!")

    while pc_result != 0 and pc_result < 17: # if pc goes above score of 17 or get a blackjack this will stop
        computer_cards.append(deal_card()) #same as in the for loop
        pc_result = calculate_score(computer_cards) #adding new value to the variable
        
        print(f"Your cards: {user_cards}, final score: {user_result}")
        print(f"Computer cards: {computer_cards} , final score: {pc_result}")
        print(compare(user_score=user_result, pc_score=pc_result))

    again_play = input("Do you want to play again? 'y' or 'n'")
    if again_play != "y":
        game_end = True
        print("BYE!")
    else:
        os.system('clear')
        game_play() #Calling the recurisve function
game_play() # Call the function for staring the program

