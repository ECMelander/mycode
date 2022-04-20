#!/usr/bin/env python3

import random

counter = 0
letter0 = "_"
letter1 = "_"
letter2 = "_"
letter3 = "_"
uAnswer =  "".join([ letter0 , letter1 , letter2 , letter3 ])
beastList = [ "bear" , "seal" , "puma" , "wolf" ]
vegeList = [ "bean" , "kale" , "corn" , "okra" ]
rockList = [ "iron" , "gold" , "lead" , "jade" ]

uPick = input("\nLet's play HANGMAN!\nPick a category: \n animal, vegetable, mineral\n> ")

if uPick.lower() == "animal":
    theAnswer = (random.choice(beastList))
elif uPick.lower() == "vegetable":
    theAnswer = (random.choice(vegeList))
elif uPick.lower() == "mineral":
    theAnswer = (random.choice(rockList))
else :
    print("Sorry, that wasn't an option")
    quit()

print(f"\n  Okay, let's play! \n ")


while counter < 10 and uAnswer != theAnswer :
    counter += 1
    uAnswer =  "".join([ letter0 , letter1 , letter2 , letter3 ])

    uGuess = (input(f"Guess what four letter {uPick} I am thinking of: \n   {uAnswer} \n Pick any letter \n> ")).lower()

    if counter == 10 :
        print(f"\n Sorry, {theAnswer.title()} was the {uPick} I was thinking of. \n Better luck next time.")
        break

    elif theAnswer.find(uGuess) == -1 :
        print(f"\n Sorry, take another guess")
        continue

    elif theAnswer.find(uGuess) == 0 :
        letter0 = uGuess
        uAnswer =  "".join([ letter0 , letter1 , letter2 , letter3 ])
        if uAnswer == theAnswer :
            print(f"Good Job! {theAnswer.title()} was the {uPick} I was thinking of!")
            break
        else :
            print("\n Nice Job! Keep going!")
            continue

    elif theAnswer.find(uGuess) == 1 :
        letter1 = uGuess
        uAnswer =  "".join([ letter0 , letter1 , letter2 , letter3 ])
        if uAnswer == theAnswer :
            print(f"Good Job! {theAnswer.title()} was the {uPick} I was thinking of!")
            break
        else :
            print("\n Nice Job! Keep going!")
            continue

    elif theAnswer.find(uGuess) == 2 :
        letter2 = uGuess
        uAnswer =  "".join([ letter0 , letter1 , letter2 , letter3 ])
        if uAnswer == theAnswer :
            print(f"Good Job! {theAnswer.title()} was the {uPick} I was thinking of!")
            break
        else :
            print(f"\n Nice Job! Keep going!")
            continue

    elif theAnswer.find(uGuess) == 3 :
        letter3 = uGuess
        uAnswer =  "".join([ letter0 , letter1 , letter2 , letter3 ])
        if uAnswer == theAnswer :
            print(f"Good Job! {theAnswer.title()} was the {uPick} I was thinking of!")
            break
        else :
            print(f"\n Nice Job! Keep going!")
            continue

    else:
        print(f"\n Sorry, {theAnswer.title()} was the {uPick} I was thinking of. \n Better luck next time.")
        break

# word = (random.choice(uPick))

# print(uPick)
# print(theWord)
# guessList[0] = uGuess
# guessList = [ letter0, letter1, letter2, letter3 ]
# uAnswer = "".join(guessList)
    # uGuess = input(f"Guess what {uPick} I am thinking of. \n It is a four letter word: {letter0}{letter1}{letter2}{letter3}. \n Go on, pick a letter \n> ")
    # uGuess = input(f"The {uPick} I am thinking of is a four letter word: {guessList}. \n Guess what it is. \n Go on, pick a letter \n>")

    # uGuess = input(f"Guess what {uPick} I am thinking of. \n It's a four letter word: {uAnswer}. \n Go on, pick a letter \n> ")



