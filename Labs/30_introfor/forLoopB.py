#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# print out all the dictionaries in farms
#for dict in farms :
#    print(dict)


# print out all the animals on the NE Farm
for NE in farms :
    if NE.get("name") == "NE Farm" :
        # print(NE.get("agriculture"))  # my basic solution
        # print(NE["agriculture"])        # Ramesh's solution
        for agri in NE.get("agriculture") :  # my attempt at cleaner output
            print(agri)
quit()
# print out the name of each farm
for i in farms :
    print(i.get("name"))
#    farmName = (i.get("name")) #, end=", ")
#    print(farmName, end=", ")

#agriGet = input(f"\nWhich farm would you like to learn about?\n {farmName}")





