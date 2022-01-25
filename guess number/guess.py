"""
The computer has the secret number ,and we are trying to guess the number
"""

import random


def guess(limit):

    guess_value = random.randint(0, limit)

    while True:
        guess = int(input(f"enter your guess between 0, {limit}: " ))
        if guess > limit:
            print("invalid guess")

        else:
            if guess < guess_value:
                print("the guess is lower than the value")
            elif guess > guess_value:
                print("the guess is higher than the value")
            else:
                print("you won !")
                break


guess(10)