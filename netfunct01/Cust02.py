#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import crayons
import os
import json

# function to send reboot command to devices

def BootMe(IPList):
    for ip in IPList:
        print(f'{crayons.red("REBOOTING")}...{ip}')



# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print (f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print (f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# start our main script
def main():
    IPBootList=[]
    """called at runtime"""
    IPFileName = input("Source file for IPs to Reboot? ")
    with open(IPFileName, "r") as FileHandle:
        for line in FileHandle:
            IPBootList.append(line.rstrip("/n"))
    BootMe(IPBootList)
    # dict containing IPs mapped to a list of physical interfaces and their state
    DictFileName = input("Source file for ip-commands? ")
    with open(DictFileName, "r") as FileHandle:
        devicecmd = json.load(FileHandle)
    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

# call our main function
main()

