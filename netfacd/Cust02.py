#!/usr/bin/env python3

import netifaces
print("Which interface would you like to see the MAC Address?")
print("Your choices are...")
print(netifaces.interfaces())
IntChoice=input(" >> ")
if IntChoice in netifaces.interfaces():
    print(netifaces.ifaddresses(IntChoice)[netifaces.AF_LINK][0]['addr'])
else:
    print("That interface does not exist")
#for i in netifaces.interfaces():
        #print('\n**************Details of Interface - ' + i + ' *********************')
        #print("EVERYTHING with netifaces.ifaddresses(i)")
        #print(netifaces.ifaddresses(i))
        #print("\n\nAF_LINK only")
        #print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
        #print("AF_LINK, first element, address key")
        #print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        #print("\n\nAF_INET only")
        #print(netifaces.ifaddresses(i)[netifaces.AF_INET])
        #print("AF_INET, first element, address key")
        #print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])


