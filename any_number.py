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
    number_guess_string = input("enter number: ")
    number_answer = random.randint(1, 9)

    # process
    try:
       number_guess = int(number_guess_string) 
       
        if number_guess == number_answer:
            print("you win!")
        else:
            print("you lose :(")
    
    except Exception:
        print("Not a valid response try again.")
    print("Done.")


if __name__ == "__main__":
    main()
