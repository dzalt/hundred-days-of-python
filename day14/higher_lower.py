from higher_lower_art import logo, vs
from higher_lower_data import data
import random
import os

def get_account():
    return random.choice(data)

def format_text(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}."

def check_answer(follower_a, follower_b):
    if follower_a > follower_b:
        return "a"
    return "b"
    
def game():
    print(logo)
    is_end = False
    score = 0
    account_a = get_account()

    while not is_end:

        account_b = get_account()

        print(f"Compare A: {format_text(account_a)}")
        print(vs)
        print(f"Compare B: {format_text(account_b)}")

        follower_a = account_a["follower_count"]
        follower_b = account_b["follower_count"]

        # print(follower_a)
        # print(follower_b)

        guess = input("Who has more follower? Type 'A' or 'B': ").lower()
        answer = check_answer(follower_a, follower_b)

        os.system("clear")
        print(logo)

        if guess == answer:
            score += 1
            print(f"You are right! Current score: {score}")
            account_a = account_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            is_end = True


game()