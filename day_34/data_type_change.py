age: int
name: str
height: float
is_human: bool

def police_check(age: int) -> bool: # expected output
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You can drive")
else:
    print("You can't")

