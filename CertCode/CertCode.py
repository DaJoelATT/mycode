#!/usr/bin/env python3

"""  This highly exciting code asks if you want a Chuck Noris Joke, and then goes
     to an API call website, pulls a random joke, and displays it.  
     Depends on :  Requests for the API call
                   json to read the data
                   crayons to make it pretty                                    """


##  Import the needed libraries to do the work

import requests
import json
import crayons

##  Make a variable so that I don't have to type the API over and over

ChuckAPI = "https://api.chucknorris.io/jokes/random"


def main():
     ## Find out if the user even knows who Chuck Norris is
     Answer = input("Do you know who Chuck Norris is? ")
     if Answer.lower() == "yes" or Answer.lower() == "y":
         resp = requests.get(ChuckAPI)
         print(resp.json().get("value"))
     else:
         print("Then... I have no words... none")


if __name__ == "__main__":
    main()
