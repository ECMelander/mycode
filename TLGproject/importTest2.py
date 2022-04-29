#!/usr/bin/env python3

import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

jsonFile = "/home/student/static/mcr6-ujqw.json"

#df= pd.read_json(jsonFile, convert_dates=['registration_date'])
df= pd.read_json(jsonFile)

#print(len(df))

df.sort_values(['registration_date'], inplace=True)
df.drop_duplicates(['apprentice_id'], inplace=True)
df.set_index(['apprentice_id'], inplace=True)

df['registration_date'] = pd.to_datetime(df['registration_date'])

print(len(df))

df["year"] = df["registration_date"].dt.year
year_filter = df['year'] >= 2013
df = df.loc[year_filter, :]

df.replace( 'Other than Vietnam era vet' , 'Veteran' , inplace = True)
df.replace( 'Vietnam era vet' , 'Veteran' , inplace = True)

print(len(df))

#print(df.veteran.unique())
#print(df[[ 'last_name' , 'first_name' , 'year' , 'veteran' , 'sex' ]].head(30))
#print(df.sex.unique())
#print(len(df))
#print(df.dtypes)
#rint(df.head())

#print(df.groupby(['year' , 'veteran']).size())


df = df[[ 'last_name' , 'first_name' , 'year' , 'veteran' , 'sex' ]]

#df.to_csv("/home/student/static/apprenticeTest.csv")




sns.countplot(x="year", hue="veteran", data=df)

plt.savefig("/home/student/static/countPlot.png")