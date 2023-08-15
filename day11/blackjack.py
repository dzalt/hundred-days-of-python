# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from blackjack_art import logo
import os

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def message(user_score, pc_score):
    if user_score == 0:
        return "You have blackjack. You win."
    elif pc_score == 0:
        return "Computer has blackjack. You lose."
    elif user_score > 21:
        return "You are bust. You Lose."
    elif pc_score > 21:
        return "PC is bust. You win."
    elif user_score > pc_score:
        return "You win."
    elif pc_score > user_score:
        return "You lose."
    elif user_score == pc_score:
        return "Draw."

def blackjack():
    print(logo)
    gameover = False
    user_cards = []
    pc_cards = []

    for i in range(2):
        user_cards.append(deal_cards())
        pc_cards.append(deal_cards())

    while not gameover:

        user_score = calc_score(user_cards)
        pc_score = calc_score(pc_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {pc_cards[0]}")
        # print(f"Computer's cards: {pc_cards}, current score: {pc_score}")

        if user_score == 0 or pc_score == 0 or user_score > 21:
            gameover = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                user_cards.append(deal_cards())
            else:
                gameover = True
    
    # Drawing cards for computer
    while pc_score != 0 and pc_score < 17:
        pc_cards.append(deal_cards())
        pc_score = calc_score(pc_cards)

    # Post Game result:
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {pc_cards}, final score: {pc_score}")
    result = message(user_score, pc_score)
    print(result)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    os.system("clear")
    blackjack()
