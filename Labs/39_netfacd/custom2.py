#!/usr/bin/env python3

import netifaces
import os

def main() :

    neti = netifaces.interfaces()
    iFace = ""
    addr = ""
    addrType = ["MAC" , "IP"]

    os.system('clear')

    print(f"Enter interface name:\n {neti}")    
    while iFace not in neti :
        iFace = input(">")

    print(f"\nEnter address type:\n {addrType}")
    while addr not in addrType :
        addr = input(">").upper()

    print()

    if addr == "MAC" :
        print(f"The MAC address of {iFace} is:\n")
        print((netifaces.ifaddresses(iFace)[netifaces.AF_LINK])[0]['addr'])

    elif addr == "IP" :
        print(f"The IP address of {iFace} is:\n")
        print((netifaces.ifaddresses(iFace)[netifaces.AF_INET])[0]['addr'])
        
    print()

main()