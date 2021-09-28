#!/usr/bin/env python3

def main():
    # Get it.  Get it Real Good
    IPList = []
    OctetNum = 1
    for LoopVar in range(4):
        print("Please enter octet #",OctetNum,end=" ")
        IPList.append(input(">>"))
        print(" ")
        OctetNum=OctetNum+1
    print("You gave me ",IPList)
    IPString = ".".join(IPList)
    print("I turned it into ",IPString)
    if IPString != "...":
        print("You gave me sumptin")
    else:
        print("You gave me nuttin")

if __name__ == "__main__":
    main()
