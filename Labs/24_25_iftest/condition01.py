#!/usr/bin/env python3

# collect user input
hostname = input("What value should we set for hostname? \n> ")

## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print()
    print("The hostname was found to be mtg")
    print("hostname matches expected config")
    print()

# Always display to user
print("Exiting the script")
