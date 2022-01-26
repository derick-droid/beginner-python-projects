"""
we want the computer to guess the number
"""

import random


def computer_guess(limit):
    low = 0
    high = limit
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"is {guess} high(h) or low(l): ")
        if feedback == "l":
            print("too low")
            low = guess + 1
        elif feedback == "h":
            print("high")
            high = guess -1
    print("congratulation computer won!")

computer_guess(10)