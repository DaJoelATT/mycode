#!/usr/bin/env python3
## create file object in "r"ead mode
Counter = 0
configlist = []
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    for ConfigLine in configfile:
        Counter += 1
        configlist.append(ConfigLine)
    #configlist = configfile.readlines()
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print("The number of lines of this file are: ",Counter)

print("Or... in one freaking line... sigh...",len(configlist))
