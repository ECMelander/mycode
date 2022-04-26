#!/usr/bin/env python3

import requests

def astros() :
    URL= "http://api.open-notify.org/astros.json"


    # requests.get() requests info from the URL
    # .json() method transforms that data into a Pythonic dictionary!
    sliceme= requests.get(URL).json()

    #print(sliceme)
    #print(type(sliceme))

    #print("People in space: " + str(sliceme["number"]))
    print(f"People in space: {sliceme['number']}")         # fPrint and dictionaries  ' ' within " "

    for a in sliceme['people'] :
        print(f"{a['name']} is on the {a['craft']}")

def iss() :
    URL= "http://api.open-notify.org/iss-now.json"
    sliceme= requests.get(URL).json()

    print("CURRENT LOCATION OF THE ISS:")
    print(f"Lon: {sliceme['iss_position']['longitude']}")
    print(f"Lat: {sliceme['iss_position']['latitude']}")



def main():
    astros()
    print()
    iss()

main()


