#!/usr/bin/env python

import pandas as pd
from sodapy import Socrata
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def main() :

    # importing data
    client = Socrata("data.wa.gov", None)               # define variable for location of source data
    results = client.get("mcr6-ujqw", limit=200000)     # import source data as results
    df = pd.DataFrame.from_records(results)             # Convert to pandas DataFrame as df

    ###for debugging###
    print(f"Starting number of rows:  {len(df)}")
    #print(results_df.columns)

    # Cleaning data
    df.sort_values(['registration_date'], inplace=True)                     # sorting by date
    df.drop_duplicates(['apprentice_id'], inplace=True)                     # removing duplicates
    df.set_index(['apprentice_id'], inplace=True)                           # setting index
    df.replace( 'Other than Vietnam era vet' , 'Veteran' , inplace = True)  # standardizing veteran designation
    df.replace( 'Vietnam era vet' , 'Veteran' , inplace = True)             # standardizing veteran designation
    df['registration_date'] = pd.to_datetime(df['registration_date'])       # converting object to date
    df["year"] = df["registration_date"].dt.year                            # adding column for year
    year_filter = df['year'] >= 2013                                        # setting filter variable
    df = df.loc[year_filter, :]                                             # applying filter variable
    df = df[['last_name', 'first_name', 'year', 'sex', 'veteran']]

    ###for debugging###
    #print(df.veteran.unique())
    #print(df[[ 'last_name' , 'first_name' , 'year' , 'veteran' , 'sex' ]].head(30))
    #print(df.sex.unique())
    print(f"Filtered rows:  {len(df)}")
    #print(df.dtypes)
    #rint(df.head())

    input()
    print()
    print(df.groupby(['year' , 'veteran']).size())
    sns.countplot(x='year', hue='veteran', data=df)
    plt.savefig('/home/student/static/countPlot2.png')

if __name__ == '__main__' :
    main()