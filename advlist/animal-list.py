#!/usr/bin/env python3

def main():
    
    # creating lists of three-letter animal names

    bugs = [ "fly" , "ant" ]
    birds = [ "hen" , "jay" ]
    fish = [ "cod" , "koi" ]

    # combining these lists
    animalGroups = [ bugs , birds , fish ]

    # display the animalGroups list
    print()
    print(animalGroups)

    # display a single animal from the animalGroups list
    print()
    print(animalGroups[1][1])

    # combining as a simple list (ungrouped) 
    #animals = bugs
    #animals.extend(birds)
    #animals.extend(fish)

    # easier combination
    animals = bugs + birds + fish 

    print()
    print(animals)

main()
