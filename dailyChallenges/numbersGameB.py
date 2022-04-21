#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

import random

def theGame():    
    num= random.randint(1,100)
    guess= "x"
    rounds= 0


    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")
        
        # COOL CODE ALERT: what is the purpose of the next fourlines?

        if guess.isdigit():
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds += 1


        elif guess < num:
            print("Too low!")
            rounds += 1


        else:
            print("Correct!")
            break
#def endGame():
    # rounds = theGame(rounds)
        if rounds == 5:
            # print(f"Sorry, the number I was thinking of was {num}")
            rePlay = input("Would you like to play again? \n (y or n) > ")
            if rePlay.lower() == "y" or "yes" :
                    theGame()
            else:
                print("Thanks for playing!")
                quit

#def main() :
theGame()
    #endGame()

#main()