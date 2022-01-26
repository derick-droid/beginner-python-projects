"""
rock paper scissor game

"""

import random


def play():

    computer_choice = random.choice(["r", "s", "p"])
    player = input("what is your choice: R is rock, s is scissors, p is paper: ").lower()

    if (player == "r" and computer_choice == "s") or (player == "s" and computer_choice == "p") or (player == "p" and computer_choice == "r"):
        print("you won")

    else:
        print("you have lost")

    print(f" computer chose:  {computer_choice} ")

play()


