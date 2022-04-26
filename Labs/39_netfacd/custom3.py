#!/usr/bin/env python3

import netifaces
import os


def mac(iFace) :
        print(f"The MAC address of {iFace} is:\n{(netifaces.ifaddresses(iFace)[netifaces.AF_LINK])[0]['addr']}")

def ip(iFace) :
        print(f"The IP address of {iFace} is:\n{(netifaces.ifaddresses(iFace)[netifaces.AF_INET])[0]['addr']}")

def main() :

    neti = netifaces.interfaces()
    iFace = ""
    addr = ""
    addrType = ["MAC" , "IP" , "BOTH"]

    os.system('clear')

    print(f"Enter interface name:\n {neti}")    
    while iFace not in neti :
        iFace = input(">")

    print(f"\nEnter address type:\n {addrType}")
    while addr not in addrType :
        addr = input(">").upper()

    print()

    if addr == "MAC" :
        mac(iFace)

    elif addr == "IP" :
        ip(iFace)

    elif addr == "BOTH" :
        mac(iFace)
        ip(iFace)

    print()

main()