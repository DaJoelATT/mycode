#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com
   
   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/
   
   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():
    """Run time code"""

    setcode = input("What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ").lower()   # collect user input for MTG card set to lookup

    # Do Set Validation


    # create resp, which is our request object
    resp = requests.get(f"{API}cards?set={setcode}")   # this "f" string reads: API + "cards/" + setcode

    # return the status code of what we just looked up
    if resp.status_code != 200:
        exit()

    # grab the json off our 200
    cardData = resp.json()

    # test if our json actually has cards in it (was it a real set?)
    if len(cardData.get('cards')) == 0:
        print(f"The code {setcode} does not appear to be a real set.")
    else:
        print(cardData)

        
#if resp  {'cards': []} in resp:
        # the .json() method will dump a JSON string into Pythonic data structures. COOL!
        # This is much easier than using the urllib.request library
#    cards = resp.json()
        #print(cards)
    #else:
    #    print("Sorry, not a valid set")



if __name__ == "__main__":
    main()

