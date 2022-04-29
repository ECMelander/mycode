#!/usr/bin/env python3


import requests

URL= "http://www.omdbapi.com/?apikey=875c4c78&s="

def main():

    try:
        choice= input("Enter a movie title:\n>")
        full_url= URL + choice
        movies= requests.get(full_url).json()
        movies['Search']
    except:
        print("We couldn't find that movie")
        exit()

    #print(movies)
    #print(full_url)

    movieList = []
    count = 0
    for m in movies['Search'] :
        count +=1
        if m['Type'] == 'movie' :
            movieList.append(m['Title'])
    #        print(f"{count}. {m['Title']} \n    released in {m['Year']}")
    print(movieList)


    #print(movies['Search'][0]['Title'])
if __name__ == "__main__":
    main()