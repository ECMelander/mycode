#!/usr/bin/env python3

move = "get"
move = move.lower().split(" ", 1)

if len(move) < 2 :
    print("less than 2")



def beginGame() :
  while True :
    begInput = input("  new  saved\n> ").lower()    
    if begInput == "new" :
      
      rooms = rpgData.rooms
      currentRoom = rpgData.currentRoom
      inventory = rpgData.inventory
      break
    elif begInput == "saved" :
      with open("output.pkl" , "rb") as dictFile :
        rooms = pickle.load(dictFile)
      with open("inventory.pkl" , "rb") as invFile :
        inventory = pickle.load(invFile)
      with open("currentRoom.pkl" , "rb") as cRoomFile :
        currentRoom = pickle.load(cRoomFile)
      break
    else :
      print("\nSorry, that's not an option\n")
      continue


    #import rpgData # as newInput

#with open("output.pkl" , "rb") as dictFile :
#    rooms = pickle.load(dictFile)
#with open("inventory.pkl" , "rb") as invFile :
#    inventory = pickle.load(invFile)
#with open("currentRoom.pkl" , "rb") as cRoomFile :
#    currentRoom = pickle.load(cRoomFile)