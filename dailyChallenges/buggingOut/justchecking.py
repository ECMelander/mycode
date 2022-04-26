#!/usr/bin/env python3
"""ECMelander | TLG at Alta3
    a scratch file for random script testing and debugging"""

name = ''
num = ''

while name == '':
    name= input("What is your name?\n>")
while num == '' :
    num= input("\nPick a number between 1 and 3\n>")
if name and num in ["1","2","3"]:
    return name, num


    def name_grabber():
    # uh oh! this while loop should force the user to answer again
    # if the user DOESN'T enter a name and DOESN'T pick a number
    # between 1 and 3!
    while True:
         name= input("What is your name?\n>")
         num= input("Pick a number between 1 and 3")
         if name and num in ["1","2","3"]:
             return name, num