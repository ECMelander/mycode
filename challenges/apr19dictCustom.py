#!/usr/bin/env python3

def main():

    pokedex={"Bulbasaur":"Grass/Poison",
             "Squirtle":"Water",
             "Charmander":"Fire"}

    # add pair to dictionary
    pokedex["Pikachu"] = "Electric"

    # print list of characters for user to choose from
    pokeList = ", ".join(pokedex.keys())
    print(pokeList)

    # prompt for input
    choice= input("Name a Generation 1 starter Pokemon:\n>")

    # original output
    # print(pokedex[choice])

    # IMPROVE the code with specified error message if the user types in a pokemon not in pokedex
    print(pokedex.get(choice, ( "Sorry, we don't have any record of that Pokemon! \n Choose from: " + pokeList )))

main()
