#!/usr/bin/env python3
"""Shawn OKeefe | TLG at Alta3
    a game of hangman"""

print(("\n")*2)
print("===== WELCOME TO HANGMAN =====",("\n")*2)


#ESTABLISH THE SECRET WORD
secret = input("Type your secret word: \n>")
secret = secret.lower()
#print(secret)
print(("\n")*30)


#BUILD THE LETTER DICTIONARY BASED ON THE SECRET WORD
list_secret = list(secret)
#print(list_secret,("\n")*2)


# PROVIDE THE NUMBER OF LETTERS
num_letters = len(secret)


print("===== LET THE GAME BEGIN =====")
print(f"The secret word has {num_letters} letters.\n")
hm_round = 1
win = 0

while hm_round <= 6 and win == 0 : 
    print(("\n")*1)
    print(f"===== ROUND - {hm_round} of 5 =====")
    hm_round = hm_round + 1
    guess= input("Guess a letter: \n>")
    if guess.lower() in list_secret:
        print(f"Your guess '{guess.lower()}' is in the secret word.\n")
        answer = input("What word do you think the secret word is?\n>")
        if answer.lower() == secret:
            print("Your answer is correct.")
            print("===== YOU WIN !!! =====")
            win = 1
        elif hm_round == 6:
            print("Wrong answer. That was your last guess.\n")
            print("===== BETTER LUCK NEXT GAME =====\n")
            break
        else:
            print("Wrong answer. Try again next round.\n")
    else:
        if hm_round <=6 and guess.lower() not in list_secret:
            print(f"Your guess '{guess.lower()}' is not in the secret word.\n")
            answer = input("What word do you think the secret word is?\n>")
            if answer.lower() == secret:
                print("Your answer is correct.")
                print("===== YOU WIN !!! =====")
                win = 1
            elif hm_round == 6:
                print("Wrong answer. That was your last guess.\n")
                print("===== BETTER LUCK NEXT GAME =====")
                break
            else:
                print("Wrong answer. Try again next round.\n")
        else: 
                print("Wrong answer. That was your last guess.\n")
                print("===== BETTER LUCK NEXT GAME =====\n")
                break

