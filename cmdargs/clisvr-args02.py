#!/usr/bin/env python3
import argparse
import socket
from datetime import datetime

def server(port,proto):
    x = "Your choice was server and it will run on port " + str(port) + " " + proto
    return x

def client(port,proto):
    x = "Your choice was client and it will run on port " + str(port) + " " + proto
    return x

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    parser.add_argument('-t', metavar='PROTOCOL', type=str, default="UDP")
args = parser.parse_args()
print("args is -->",args)
print("choices[args.role] is ->",choices[args.role])
print("args.role is ->",args.role)
print("args.p is ->",args.p)
print("args.t is ->",args.t)
function = choices[args.role]
print(function(args.p,args.t))

