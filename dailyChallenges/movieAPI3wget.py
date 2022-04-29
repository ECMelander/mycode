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

    count = 0
    for m in movies['Search'] :
        count +=1
        if m['Type'] == 'movie' :
            print(f"{count}. {m['Title']} \n    released in {m['Year']}")






    print(movies['Search'][0]['Title'])

    dL=input("Would you like to download a movie poster? \n ( y / n )\n >")
    if dL.lower() == 'y' or 'yes' :
        poster = input("Which movie poster would you like? \n Enter just the number from above \n >")

wget.download(urlCSV, "/home/student/static/")

if __name__ == "__main__":
    main()