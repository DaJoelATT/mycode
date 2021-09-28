#!/usr/bin/env python3
import os
import subprocess 
def main():
    print("What would you like?")
    print("1. Invoke VIM")
    print("2. invoke ping")
    print("3. Figure out postage")
    print("4. Book Review")
    print("5. Letter grade review")

    ChoicStr = input("Your choice 1-5 ")

    if ChoicStr == "1":
        subprocess.call("vim")
    elif ChoicStr == "2":
        #subprocess.call("ping","8.8.8.8")
        result = os.system("ping -c 2 8.8.8.8")

        # we a runcode stored in "result"
        # test if that runcode was successful
        if result == 0:  # oddly, a runcode of 0 means success!
            print("We can reach the google DNS servers!")
        else: # any other number is a failure
            print("Having trouble contacting google DNS :(")   
    
    elif ChoicStr == "3":
        WeightStr = input("How much does it weigh? ")
        WeightFlo = float(WeightStr)
        if WeightFlo >= 10:
            print("Heavy!!")
        else:
            print("Light!!")
    elif ChoicStr == "4":
        print("Wait!! You can read??")
    elif ChoicStr == "5":
        print("Grades!!")

main()

