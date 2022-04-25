#!/usr/bin/env python3

"""ECMelander | TLG at Alta3
    parsing the entire book, Dracula"""

vampFile = open("345-0.txt" , "r")

vampList = vampFile.readlines()

# Loop over every line in Dracula, print each line out!
#for x in vampList :
#    print(x, end="")

# Print the lines containing the word vampire (not case sensitive)
for x in vampList :
    if "vampire" in x.lower() :
        print(x, end="")


# Count the lines containing the word vampire (not case sensitive)
for x in vampList :
    if "vampire" in x.lower() :
        print(vampList.count(x))




vampFile.close()
