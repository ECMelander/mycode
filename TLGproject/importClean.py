#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata
import requests

# define variable for location of source data
client = Socrata("data.wa.gov", None)

# import source data
results = client.get("mcr6-ujqw", limit=200000)

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results)

###for debugging###
print(len(df))
#print(results_df.columns)

# removing duplicates and setting index
df.sort_values(['registration_date'], inplace=True)
df.drop_duplicates(['apprentice_id'], inplace=True)
df.set_index(['apprentice_id'], inplace=True)

###for debugging###
#print(len(df))

# Cleaning data
df['registration_date'] = pd.to_datetime(df['registration_date'])       # converting object to date
df["year"] = df["registration_date"].dt.year                            # adding column for year
df.replace( 'Other than Vietnam era vet' , 'Veteran' , inplace = True)  # standardizing veteran designation
df.replace( 'Vietnam era vet' , 'Veteran' , inplace = True)             # standardizing veteran designation

###for debugging###
#print(df.veteran.unique())
#print(df[[ 'last_name' , 'first_name' , 'year' , 'veteran' , 'sex' ]].head(30))
#print(df.sex.unique())
#print(len(df))
#print(df.dtypes)
#rint(df.head())

print(df.groupby(['year' , 'veteran']).size())