#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        print("EVERYTHING with netifaces.ifaddresses(i)")
        print(netifaces.ifaddresses(i))
        print("\n\nAF_LINK only")
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
        print("AF_LINK, first element, address key")
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print("\n\nAF_INET only")
        print(netifaces.ifaddresses(i)[netifaces.AF_INET])
        print("AF_INET, first element, address key")
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])


