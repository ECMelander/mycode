#!/usr/bin/env python3

def main():
    
    # Marvel Characters dictionary - given values
    marvelchars= {
    "Starlord":
        {"real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"},

    "Mystique":
        {"real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"},

    "Hulk":
        {"real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"}
        
        }


    # user input
    char_name = input("Which character do you want to know about? \n (Starlord, Mystique, Hulk) \n>")
    char_stat = input("What statistic do you want to know about? \n (real name, powers, archenemy) \n>")
  
    # basic output
    print(f"{char_name}'s {char_stat} is/are: {marvelchars[char_name][char_stat].title()}")

    # trying to use .get
    print(f"{char_name}'s {char_stat} is: {marvelchars.get({char_name}.get({char_stat}))}")

main()
