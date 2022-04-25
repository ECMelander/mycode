#!/usr/bin/env python3

inventory = []
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
