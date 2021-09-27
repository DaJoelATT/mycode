#!/usr/bin/env python3
## It really bugged me that there wasn't a space.  
# so I added one

ip_input = input("Please enter an IPv4 IP address: ")

## the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + ip_input) ; Concatinated, no space

## print() can be given a series of objects separated by a comma, adds a space, or the spacer 
# character which is controlled by the sep="" modifier

print("You told me the IPv4 address is:", ip_input,sep=" -> ")

## Now adding Vendor info to the script.

vendor_input = input("Please tell me the vendor for this device: ")

# Printing it out

print("You told me the Vendor was:",vendor_input,sep=" -$$- ")

# putting it all together

print("Therefore,",ip_input,"is a",vendor_input,"device.",sep="  ")

