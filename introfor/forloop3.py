#!/usr/bin/python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


for farmName in farms:
    print(farmName.get("name","Unknown Farm"), end=":\n")
    for CritterName in farmName.get("agriculture"):
        print(" -",CritterName)


