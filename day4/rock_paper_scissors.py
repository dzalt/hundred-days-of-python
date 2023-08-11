rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line

import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user > 2 or user < 0:
    print("Invalid Input. You Lose.")
else:
    pc = random.randint(0, 2)

    # 0 beats 2 but loses to 1
    # 1 beats 0 but loses to 2
    # 2 beats 1 but loses to 0

    img = [rock, paper, scissors]

    print("You chose:")
    print(img[user])
    print("Computer chose:")
    print(img[pc])

    if user == 0 and pc == 2:
        print("You Win.")
    elif user == 2 and pc == 0:
        print("You Lose.")
    elif user > pc:
        print("You Win.")
    elif pc > user:
        print("You Lose.")
    elif user == pc:
        print("Draw.")
