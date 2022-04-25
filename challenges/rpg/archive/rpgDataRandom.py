#!/usr/bin/env python3

import random

currentRoom = 'Hall'
rooms = {



            'Kitchen' : {
                  'north' : 'Hall',
                  'south' : 'Pantry',
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

#monsterRoom = (random.choice([ 'Kitchen' , 'Pantry' , 'Library' ]))
#rooms[monsterRoom]['item' : 'monster']

rooms['Hall'] = {
            'south' : 'Kitchen',
            'east'  : 'Dining Room',
            'item'  : 'key'
            }

#rooms.update("rooms2")

#monsterDict = (rooms[monsterRoom])
#monsterDict.update['item':'monster']

print(monsterDict)