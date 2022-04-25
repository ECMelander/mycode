#!/usr/bin/env python3

import pickle

#file = open("output.pkl" , "rb")

#rooms = pickle.loads(file)

#print(type(rooms))
#print(rooms)

#file.close()

with open("output.pkl" , "rb") as file :
    rooms = pickle.load(file)

print(type(rooms))
print(rooms)

