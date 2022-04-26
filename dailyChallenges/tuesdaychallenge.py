#!/usr/bin/env python3

mylist= [1,2,3,4,5, "Python"]

name= input("What is your name? \n>")

# This is what you should see when print runs-
# Hi <name>! Welcome to Day 2 of Python Training!

# class answer 
# print("Hi " + name.capitalize() + "! Welcome to Day " + str(mylist[1]) + " of " + mylist[5] + " Training!")

# my attempt to fix with f string
print(f"Hi {name.capitalize()}! Welcome to Day {mylist[1]} of {mylist[5]} Training!")

# original with errors
# print("Hi " + name.capitalize + "! Welcome to Day " + mylist[1] + " of " + mylist[6] " Training!")
