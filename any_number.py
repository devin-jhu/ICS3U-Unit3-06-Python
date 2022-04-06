#!/usr/bin/env python3

# Created by Devin Jhu
# Created on March 2022
# The number game

import random


def main():
    # this function is a guessing game

    print("The number game")
    print("Guess a number between 1 and 9")

    # input
    guess_number_string = input("Enter your guess: ")
    random_number = random.randint(0, 9)

    # process
    try:
        guess_number = int(guess_number_string)

        if guess_number == random_number:
            print("You win!")
        else:
            print("You lose :( ")

    except Exception:
        print("Not a number")
    print("\nDone.")


if __name__ == "__main__":
    main()
