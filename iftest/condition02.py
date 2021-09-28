#!/usr/bin/env python3

def main():
    # Get what we want for a hostname
    hostname = input("What do you want to call it? ")
    if hostname == "MTG":
        print("The hostname was found to be MTG")
    else: 
        print("You named it ",hostname," not MTG")

if __name__ == "__main__":
    main()
