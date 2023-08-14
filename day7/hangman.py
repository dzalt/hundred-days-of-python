import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

# Choosing the word

chosen_word = random.choice(word_list)
print("Solution: " + chosen_word)

# Making display blanks

display = []

for i in range(len(chosen_word)):
    display += "_"

# The Game

gameover = False
lives = 6
print(logo)

while not gameover:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            gameover = True
            print("You Lose")
    
    print(" ".join(display))

    if "_" not in display:
        gameover = True
        print("You Win")
    
    print(stages[lives])
