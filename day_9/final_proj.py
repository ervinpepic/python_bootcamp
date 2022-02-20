from start_logo import logo
print(logo)

biding_is_over = False
a = 0
b = 0
final = 0

while not any_other_biders:
    name = input("Entery your name => ")
    bid = int(input("Entery your bid value => $"))
    other_biders = input("Any other biders? Type yes for continue entering name or no for exit the program: \n")
    final_bid = {
        "name": name,
        "bid": bid
    }
    for _ in final_bid:
        if final_bid["bid"] > a:
            a = final_bid["bid"]
            b = a
            final = b
    if other_biders.lower() == "no":
        any_other_biders = True
        print("Bye")

print(f"The winner is {name} with a bid of ${final}")

# Or we can use a function aproach
biders_concurrency = {}

def find_the_winner(biding_winner):
    highest_bid = 0
    winner_name = ""
    for winner in biding_winner:
        bider = biding_winner[winner]
        if bider > highest_bid:
            highest_bid = bider
            winner_name = winner
    print(f"Winner is {winner_name} with a bid of {highest_bid}")

biding_is_over = False
while not biding_is_over:
    name = input("Entery your name => ")
    bid = int(input("Entery your bid value => $"))
    other_biders = input("Any other biders? Type 'yes' for continue or 'no' for exit the program: \n")
    biders_concurrency[name] = bid

    if other_biders == "no":
        biding_is_over = True
        find_the_winner(biders_concurrency)
