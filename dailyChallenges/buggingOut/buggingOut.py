#!/usr/bin/env python3
import sys
import time
import os



# there's nothing wrong with this function, it's just some cool code!
def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def main():

    os.chdir(/home/student/mycode/dailyChallenges/buggingOut/)

    name = ''
    num = ''

    while name == '':
        name= input("What is your name?\n>")
    while num == '' :
        num= input("\nPick a number between 1 and 3\n>")


    num_dict= {"1":"great","2":"awesome","3":"superb" }
    with open("horoscope.txt", "w") as fileobj:
        fileobj.write(f"{name}, I predict today will be {num_dict[num].upper()}!")

    # Not an error per se, but it's undesirable that
    # this gets written out with no spaces!
    # Fix the for loop to give a nicer output!
    for x in ["YOUR ", "FUTURE ", "HAS ", "BEEN ", "WRITTEN ", "TO ", "HOROSCOPE.TXT...\n"]:
        print1by1(x)

main()
