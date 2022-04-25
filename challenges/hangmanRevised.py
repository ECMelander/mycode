#!/usr/bin/env python3
"""ECMelander | TLG at Alta3
    my updated hangman game"""

import os
import random


def main() :

    counter = 0
    wordBank = [{"animal" : [ "bear" , "seal" , "puma" , "wolf" ],
                "vegetable" : [ "bean" , "kale" , "corn" , "okra" ],
                "mineral" : [ "iron" , "gold" , "lead" , "jade" ]
                }]

    os.system("clear")
    print("\nLet's Play Hangman!\n")

    for x in wordBank :
        while counter < 4 :
            uCategory = input("\nPick a category: \n animal, vegetable, mineral\n> ")
            if uCategory.lower() in (x.keys()) :
                random.shuffle(x[uCategory])
                theAnswer = (x[uCategory][0])

                break
            else :
                print("\nSorry, that wasn't an option")
                counter += 1
                continue

    answerLen = len(theAnswer)
    blankList = (list("_"*answerLen))
    blankJoin = "".join(blankList)
    answerList = (list(theAnswer))
    answerList.append(x[uCategory][0])

    os.system("clear")
    print(f"\n  Okay, let's play! \n ")


    while counter < 10 and blankJoin != theAnswer :
        counter += 1
        uGuess = input(f"\nGuess what {uCategory} I am thinking of.  It has {answerLen} letters: \n   {blankJoin} \n\n Pick any letter \n> ").lower()

        if counter == 10 :
            os.system("clear")
            print(f"\n Sorry, {theAnswer.title()} was the {uCategory} I was thinking of. \n Better luck next time.")
            break

        if uGuess in answerList :
            x = int(answerList.index(uGuess))
            blankList.pop(x)
            blankList.insert(x,uGuess)
            blankJoin = "".join(blankList)
            if blankJoin == theAnswer :
                os.system("clear")
                print(f"\nGood Job! {theAnswer.title()} was the {uCategory} I was thinking of!\n")
                break
            else :
                os.system("clear")
                print(f"\n Nice Job! Keep going!")
                continue
        elif uGuess not in answerList :
            os.system("clear")
            print(f"\n Sorry, no {uGuess.capitalize()}. Take another guess")
            continue
        else:
            os.system("clear")
            print(f"\n Sorry, {theAnswer.title()} was the {uCategory} I was thinking of. \n Better luck next time.")
            break    
            

main()