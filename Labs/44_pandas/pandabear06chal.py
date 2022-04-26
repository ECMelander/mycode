#!/usr/bin/env python3

import pandas as pd

def main():
    inType = input("\nWhat type of file would you like to conver?\n csv  json  xls \n > ").lower()
    frameIN = input("\nWhat file would you like to convert?\n Please enter the name (including full path) of the file you would like to convert?\n > ")
    outType = input("\nWhat type of file would you like to convert this to:\n csv  json  xls \n > ").lower()
    frameOUT = input("\nWhere would you like to save the new file, and what name should we give it?\n Please enter the full path including the new name\n > ")

    if inTpye == csv or .csv :
        frameIN = pd.read_csv(frameIN)

    elif inTpye == json or .json :
        frameIN = pd.read_json(frameIN)

    elif inTpye == xls or .xls :
        frameIN = pd.read_xls(frameIN)

    else :
        print("Sorry, this script currently only supports 
    # create a dataframe ciscocsv
#    frameIN = pd.read_csv("ciscodata.csv")
    # create a dataframe ciscojson
#    ciscojson = pd.read_json("ciscodata2.json")

    ## export to json
    ## do not include index number
    frameIN.to_json("ciscodataCSV.json", orient="records")

    ## export to csv
    ## do not include index number
#    ciscodf.to_csv("combined_ciscodata.csv", index=False)

    ## export to Excel
    ## do not include index number to xls
#    ciscodf.to_excel("combined_ciscodata.xls", index=False)
    ## do not include index number to xlsx
#    ciscodf.to_excel("combined_ciscodata.xlsx", index=False)

if __name__ == "__main__" :
    main()

