# Variables scope

enemies = 1 #global scope
player_health = 10 #global scope
def increasee_enemies():
    enemies = 2
    print(f"Enemies iniside func: {enemies}")

increasee_enemies()
print(f"Enemies outside function {enemies}")

#Local scope
def drink_potion():
    potion_strength = 2 # Local scope variable
    print(potion_strength)

drink_potion()

#if we call potion_strength outside of the function, it will throw
# an error, beacuse of local scope

# No Block scope
if 3 > 2:
    a = 10 #available otuside if statement

game_level = 3
def create_enemy():
    enemies = ['Skeleton', 'Zombie', 'Alien']

    if game_level < 5:
        new_enemy = enemies[0] #available otuside if statement but not outisde function
    print(new_enemy)

#global scope modify
enemy = "Skeleton"
def increase_enemy():
    global enemy #not recomended
    enemy += "Rex" 

# GLOBAL CONSTANTS

PI = 3.14159
URL = "someurl"
TWITTER_API = "https///dsfddsaf/dsafsaf/sdf"
