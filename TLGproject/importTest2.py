#!/usr/bin/env python

import requests
import pandas as pd

jsonFile = "/home/student/static/mcr6-ujqw.json"

df= pd.read_json(jsonFile, convert_dates=['registration_date'])

#print(len(df))

df.sort_values(['registration_date'], inplace=True)
df.drop_duplicates(['apprentice_id'], inplace=True)
df.set_index(['apprentice_id'], inplace=True)

#print(len(df))

df["year"] = df["registration_date"].dt.year

df.replace( 'Other than Vietnam era vet' , 'Veteran' , inplace = True)
df.replace( 'Vietnam era vet' , 'Veteran' , inplace = True)


#print(df.veteran.unique())
#print(df[[ 'last_name' , 'first_name' , 'year' , 'veteran' , 'sex' ]].head(30))
#print(df.sex.unique())
#print(len(df))
#print(df.dtypes)
#rint(df.head())

print(df.groupby(['year' , 'veteran']).size())