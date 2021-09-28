#!/usr/bin/env python3
import subprocess
# open file in read mode
dnsfile = open("dnsservers.txt", "r")
# create list of lines
dnslist = dnsfile.readlines()
# loop over lines
for svr in dnslist:
    #print and end without a newline
    print(svr, end="")
    subprocess.call(["ping","-c 2",svr])
# close your file
dnsfile.close()

