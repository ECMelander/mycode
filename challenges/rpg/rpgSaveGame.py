#!/usr/bin/python3
""" ECMelander | TLG at Alta3
    modifications to existing game to allow player to save game"""

# Game allows players to save and quit game.  Only one game can be saved/retrieved.
# This script depends on one additional script and three pickle files:
    # rpgData.py 
    # currentRooms.pkl 
    # inventory.pkl 
    # rooms.pkl 

import os
import pickle

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  quit
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")


# define options when exiting game: save, quit without saving, or resume current game    
def exitGame() :
  os.system('clear')
  print("\nThanks for playing!")
  while True :
    quiType = input("\n  quit  save  resume \n\n> ").lower()
    if quiType == "quit" :
      print("\nGoodbye\n\n")
      quit()
    elif quiType == "save" :
      with open("rooms.pkl" , "wb") as dictFile :
        pickle.dump(rooms, dictFile)
      with open("inventory.pkl" , "wb") as invFile :
        pickle.dump(inventory, invFile)
      with open("currentRoom.pkl" , "wb") as cRoomFile :
        pickle.dump(currentRoom, cRoomFile)
      print("\nGame saved \n\n  Goodbye\n\n")
      quit()
    elif quiType == "resume" :
      os.system('clear')
      break
    else :
      print("\nSorry, that's not an option\n")
      continue


#start by clearing the screen and displaying status
os.system("clear")
showInstructions()

# Let player select to retrieve a saved game or start a new game
print("\nWould you like to start a new game or resume a saved game?\n")
while True :
  begInput = input("  new  saved\n> ").lower()    
  if begInput == "new" :
    import rpgData
    rooms = rpgData.rooms
    currentRoom = rpgData.currentRoom
    inventory = rpgData.inventory
    break
  elif begInput == "saved" :
    with open("rooms.pkl" , "rb") as dictFile :
      rooms = pickle.load(dictFile)
    with open("inventory.pkl" , "rb") as invFile :
      inventory = pickle.load(invFile)
    with open("currentRoom.pkl" , "rb") as cRoomFile :
      currentRoom = pickle.load(cRoomFile)
    break
  else :
    print("\nSorry, that's not an option\n")
    continue
os.system("clear")

#loop forever
while True:
  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  # option to exit game
  if move[0] == 'quit' :
    exitGame()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
      os.system("clear")
    #there is no door (link) to the new room
    else:
        print('\nYou can\'t go that way!')
        input("\n Press enter to continue")
        os.system("clear")

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] == rooms[currentRoom]['item'] :
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      os.system("clear")
      print(f"\n {move[1].title()} got!\n")
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('\nCan\'t get ' + move[1] + '!')
      input("\n Press enter to continue")
      os.system("clear")
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'book' in inventory:
    print('\nYou escaped the house with the ultra rare key, the book of spells, and the magic potion... YOU WIN!\n\n')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    if 'cookie' in inventory :
      print("\nYou see a hungry monster. You instinctively offer him the cookie.\n The monster takes the cookie and runs away.\n")
      del rooms[currentRoom]['item']
      inventory.remove("cookie")
    else :
      print('\nA hungry monster ate you... GAME OVER!\n')
      break

 # else:
 #   print("\nSorry, that wasn't an option\n\n")

