#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from guess_the_number_art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num = random.randint(1, 100)
print(f"Solution: {num}")

attempt = 0
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempt = 10
else:
    attempt = 5

is_end = False

while not is_end:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == num:
        print(f"You got it! The answer was {num}.")
        is_end = True
    else:
        if guess > num:
            print("Too High")
        elif guess < num:
            print("Too Low")
        
        attempt -= 1

        if attempt == 0:
            print("You've run out of guesses, you lose.")
            is_end = True