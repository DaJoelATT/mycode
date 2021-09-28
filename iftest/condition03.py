#!/usr/bin/env python3

def main():
    # Get the hostname
    hostname = input("What do you want it to be?? ")
    # BUT... WAIT!!   Lets process it to be all lowercase
    # Make it lower
    print("Lower ---> ",hostname.lower())
    print("Upper ---> ",hostname.upper())
    print("Title ---> ",hostname.title())
    capChoice = input("Which would you like (L,U,T)?")
    if capChoice.lower() == "l":
        hostname = hostname.lower()
    elif capChoice.upper() == "U":
        hostname == hostname.upper()
    elif capChoice.lower() == "t":
        hostname = hostname.title()
    else:
        print("Come on man!  pick one of the 3 choices")
    print("The Hostname is now ---> ",hostname)


if __name__ == "__main__":
    main()


