import random
from data import data
from art import logo, vs

def generate_acc():
    return random.choice(data)

def format_acc(acc):
    name = acc["name"]
    desc = acc["description"]
    ct = acc["country"]
    return f"{name}, a {desc}, from {ct}"

def compare(guess, acc1, acc2):
    if acc1 > acc2:
        return guess == "a"
    elif acc2 > acc1:
        return guess == "b"
    else:
        return "Wrong choice"


def gameplay():

    game_end = False

    compare_1 = generate_acc()
    compare_2 = generate_acc()

    score = 0

    while not game_end:
        compare_1 = compare_2
        compare_2 = generate_acc()

        while compare_1 == compare_2:
            compare_2 = generate_acc()

        print(f"Compare A: {format_acc(compare_1)}")
        print(vs)
        print(f"Against B: {format_acc(compare_2)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        compare_1_fw_count = compare_1["follower_count"]
        compare_2_fw_count = compare_2["follower_count"]

        check_answer = compare(guess, compare_1_fw_count, compare_2_fw_count)

        if check_answer:
            score += 1
            print(f"You're right, your current score is {score}")
        else:
            game_end = True
            print(f"Game Over. Score: {score}")
        
gameplay()


# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.



#TEsting logic
# print(logo)
# print(f"Compare A: {data[first_num]['name']}, a {data[first_num]['description']}, from {data[first_num]['country']} with => {data[first_num]['follower_count']} follwers")
# print(vs)
# print(f"Against B: {data[second_num]['name']}, a {data[second_num]['description']}, from {data[second_num]['country']} with => {data[second_num]['follower_count']} follwers")

# vs = input("Who has more followers? Type 'A' or 'B': ").lower()

# if data[first_num]['follower_count'] > data[second_num]['follower_count']:
#     print("YES VECE JE")
#     compare.append(data[first_num]["follower_count"])
#     counter += 1
# elif data[second_num]['follower_count'] > data[first_num]['follower_count']:
#     compare.append(data[second_num]["follower_count"])
#     counter += 1
# else:
#     print(f"You loose, your score is {counter}")

# print(f"you have {counter} score your result is {compare}")