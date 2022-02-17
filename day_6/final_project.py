def tr():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        tr()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()