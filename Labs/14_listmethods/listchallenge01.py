#!/usr/bin/env python3

## given lists
icecream= ["indentation", "spaces"]
tlgstudents= ["Akino", "Bai", "Carlos", "Dalton", "Dan", "Edith", "Ethan", "Isaiah", "J", "Jessica", "John", "Justin", "Khalil", "Nikk", "Ramesh", "Scotty", "Sergio", "Shawn"]

## append to given list
icecream.append(4)

## confirm append(4) yielded integer
# print(type(icecream[2]))

## collect user input
student_name = input("Pick a number between 0 and 17:  ")

## better way to collect input
# student_name = int(input("Pick a number between 0 and 17:  "))

## output to print
print(tlgstudents[int(student_name)] , "always uses" ,  icecream[2] , icecream[1] , "to indent." )
