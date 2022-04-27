#!/usr/bin/env python3

import requests

# print url for image
def url(pokeapi) :
    print(pokeapi['sprites']['front_default'])

def url2(pokeapi) :
    import wget
    imgurl = pokeapi['sprites']['front_default']
    wget.download(imgurl, "/home/student/static/")

# slice dictionary to return list of moves
def moves(pokeapi) :
    for x in pokeapi['moves'] :
        print(x['move']['name'])

# count dictionaries within game_indices
def games(pokeapi) :
    print(len(pokeapi['game_indices']))

# count dictionaries within game_indices using for loop
def games2(pokeapi) :
    count = 0
    for x in pokeapi['game_indices'] :
        count += 1
    print(count)

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    games2(pokeapi)

main()