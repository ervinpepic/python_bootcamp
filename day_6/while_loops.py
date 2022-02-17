def tr():
    turn_left()
    turn_left()
    turn_left()
 
def jump():
    move()
    turn_left()
    move()
    tr()
    move()
    tr()
    move()
    turn_left()
    
# for i in range(0, 6):
#     jump()

number_of_hr = 6

while number_of_hr > 0:
    jump()
    number_of_hr -= 1

def tr():
    turn_left()
    turn_left()
    turn_left()
 
def jump():
    move()
    turn_left()
    move()
    tr()
    move()
    tr()
    move()
    turn_left()
number_of_hr = 6

while not at_goal():
    jump()

# Hurdles 3

def tr():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_in_front():
        turn_left()
        move()
        tr()
        move()
        tr()
        move()
        turn_left()
    elif front_is_clear():
        move()
    else:
       break

# or another way

def tr():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    tr()
    move()
    tr()
    move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
       move()


# hurdles 4

def tr():
    turn_left()
    turn_left()
    turn_left()
def jump():
    tr()
    move()
    tr()
    move()
while not at_goal():
    while not wall_on_right():
        if not wall_on_right():
            jump()
    if wall_in_front():
        turn_left()
    else:
       move()
# or another way

def tr():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    tr()
    move()
    tr()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()