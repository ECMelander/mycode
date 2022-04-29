#!/usr/bin/env python3


import requests

URL= "http://www.omdbapi.com/?apikey=875c4c78&s="

def main():
    choice= input("Enter a movie title:\n>")

    full_url= URL + choice

    movies= requests.get(full_url).json()

    #print(movies)
    #print(full_url)

    for m in movies['Search'] :
        if m['Type'] == 'movie' :
            print(f"{m['Title']} was released in {m['Year']}")

if __name__ == "__main__":
    main()