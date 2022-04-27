#!/usr/bin/env python3

import netifaces
import os


def mac(macFace) :
        print(f"MAC address : {(netifaces.ifaddresses(macFace)[netifaces.AF_LINK])[0]['addr']}")

def ip(ipFace) :
        print(f" IP address : {(netifaces.ifaddresses(ipFace)[netifaces.AF_INET])[0]['addr']}")

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

    print(f"\n     ====== {iFace} =====")

    if addr == "MAC" :
        mac(iFace)

    elif addr == "IP" :
        ip(iFace)

    elif addr == "BOTH" :
        mac(iFace)
        ip(iFace)

    print()

main()