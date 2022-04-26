#!/usr/bin/env python3

import netifaces
import os

def main() :

    neti = netifaces.interfaces()
    iFace = ""
    addr = ""
    addrType = ["MAC" , "IP"]

    os.system('clear')
    while iFace not in neti :
        iFace = input(f"Enter interface name:\n {neti}\n>")

    while addr not in addrType :
        addr = input(f"\nEnter address type:\n {addrType}\n>").upper()

    print()

    if addr == "MAC" :
        print(f"The MAC address of {iFace} is:\n")
        print((netifaces.ifaddresses(iFace)[netifaces.AF_LINK])[0]['addr'])

    elif addr == "IP" :
        print(f"The IP address of {iFace} is:\n")
        print((netifaces.ifaddresses(iFace)[netifaces.AF_INET])[0]['addr'])
        
    print()

main()