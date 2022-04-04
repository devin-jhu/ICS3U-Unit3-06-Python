#!/usr/bin/env python3

# Created by Devin Jhu
# Created on March 2022
# The number game

import constants


def main():
    # this function is a guessing game

    print("The number game")
    print("Guess a number between 1 and 9")

    # input
    NumberGuess = int(input("enter number: "))

    # process
    if NumberGuess == constants.NumberAnswer:
        print("you win!")
    else:
        print("you lose :(")
    print("Done.")


if __name__ == "__main__":
    main()
