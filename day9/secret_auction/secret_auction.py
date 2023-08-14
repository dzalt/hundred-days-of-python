import os
from secret_auction_art import logo

is_end = False
bids = {}

def highest_bid(bids):
    winner = ""
    win_bid = 0
    for i in bids:
        if bids[i] > win_bid:
            winner = i
            win_bid = bids[i]
    
    print(f"The winner is {winner} with a bid of ${win_bid}.")

print(logo)

while not is_end:
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bids[name] = bid

    if input("Are there any other bidders? Type 'yes' or 'no':\n").lower() == "yes":
        os.system("clear")
    else:
        highest_bid(bids)
        is_end = True
