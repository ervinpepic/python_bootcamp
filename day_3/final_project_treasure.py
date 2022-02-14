__header__ = '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/___/____
*******************************************************************************'''
print(__header__)
# 
# 
# 

print("Welcome to Treasure Islan. \n Your mission is to find the treasure")

first_q = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ').lower()

if first_q != 'left':
    print("You fell into a hole. Game Over.")
elif first_q == 'left':
    second_q = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if second_q != 'wait':
        print("You get attacked by an angry trout. Game Over.")
    elif second_q == 'wait':
        third_q = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if third_q != 'blue' and third_q != 'red' and third_q != 'yellow':
            print("You chose a door that doesn't exist. Game Over.")
        elif third_q == 'blue':
            print("You enter a room of beasts. Game Over.")
        elif third_q == 'red':
            print("It's a room full of fire. Game Over.")
        elif third_q == 'yellow':
            print("You found the treasure! You Win!")


    