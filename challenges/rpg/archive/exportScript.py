#!/usr/bin/env python3

# Python program to write JSON
# to a file


#import json
import pickle

# Data to be written




currentRoom = 'Hall'
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'south' : 'Pantry',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'cookie',
                  'north' : 'Library',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'north' : 'Kitchen',
                  'item' : 'potion',
               },
            'Library' : {
                  'south' : 'Dining Room',
                  'item' : 'book',
            }
         }

#with open("output.json", "w") as outfile:
#	json.dump(rooms, outfile)

##pickle
#f = open("output.pkl" , "wb")

#pickle.dump(rooms,f)

#f.close()

with open("output.pkl" , "wb") as file :
      pickle.dump(rooms, file)


#with open("output.py","w") as output :
#    for i in rooms :
#        output.write(i)
