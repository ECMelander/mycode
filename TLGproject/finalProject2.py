#!/usr/bin/env python3
""" ECMelander | TLG at Alta3
    Filtering and displaying data for veterans in apprenticeships
    Data from data.wa.gov"""

import pandas as pd
from sodapy import Socrata
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


def totalVets(df_V) :
    ### unstacking the groupby
    df_V = df_V.groupby(['year' , 'veteran']).agg({'veteran' : 'count'})
    df_V = df_V.unstack()
    #print(df_gbU)

    #df_gbU_copy = df_gbU.copy()
    df_V.columns = ['__'.join(col).strip() for col in df_V.columns.values]
    #print(df_gbU_copy)

    df_V['total'] = df_V.sum(axis=1)
    df_V['Percentage'] = df_V['veteran__Veteran'] / df_V['total']
    df_V['Percentage'] = pd.Series(['{:.2f}%'.format(val * 100) for val in df_V['Percentage']], index = df_V.index)
    df_V['Veterans'] = df_V['veteran__Veteran'].astype(int)
    #print(df_gbU_copy)
    df_V = df_V[['Veterans', 'Percentage']]
    print(f"\nTotal Veteran Apprenticeship Participation\n      from {yrMin} to {yrMax}\n")    
    print(df_V)    

def femaleVets(df_F) :
    sex_filter = df_F['sex'] == 'Female'                                             # setting filter variable
    df_F = df_F.loc[sex_filter, ['year', 'sex', 'veteran']]       # applying filter variable
    df_F = df_F.groupby(['year' , 'veteran']).agg({'veteran' : 'count'})
    df_F = df_F.unstack()
    df_F['Female_Vet'] = df_F[[('veteran', 'Veteran')]]    
    #df_F.columns = ['__'.join(col).strip() for col in df_F.columns.values]
    #df_F['Percent_Change'] = df_F['veteran__Non-vet'].pct_change()    
    #print(df_F.pct_change())
    #input()

    df_F['Percent_Change'] = df_F['Female_Vet'].pct_change(fill_method='ffill')
    df_F['Percent_Change'] = pd.Series(['{:.2f}%'.format(val * 100) for val in df_F['Percent_Change']], index = df_F.index)
    #df_F['Female_Vet'] = df_F['Female_Vet'].astype(int)
    #df_F['Percent_Change'] = df_F.pct_change([('veteran', 'Non-vet')])
    df_F = df_F[['Female_Vet', 'Percent_Change']]
    print(f"\nFemale Veteran Apprenticeship Participation\n      from {yrMin} to {yrMax}\n")    
    print(df_F)    



def main() :

    global yrMax
    global yrMin

    # importing data
    client = Socrata("data.wa.gov", None)               # define variable for location of source data
    results = client.get("mcr6-ujqw", limit=200000)     # import source data as results
    df = pd.DataFrame.from_records(results)             # Convert to pandas DataFrame as df

    ###for debugging###
    print(f"\nStarting number of rows:  {len(df)}")

    # Cleaning data
    df.sort_values(['registration_date'], inplace=True)                     # sorting by date
    df.drop_duplicates(['apprentice_id'], inplace=True)                     # removing duplicates
    df.set_index(['apprentice_id'], inplace=True)                           # setting index
    df.replace( 'Other than Vietnam era vet' , 'Veteran' , inplace = True)  # standardizing veteran designation
    df.replace( 'Vietnam era vet' , 'Veteran' , inplace = True)             # standardizing veteran designation
    df['registration_date'] = pd.to_datetime(df['registration_date'])       # converting object to date
    df["year"] = df["registration_date"].dt.year                            # adding column for year

    # setting variable to filter by year
    yrList = list(df['year'].unique())          # creating list for validating user input
    yrMax = max(yrList)
    yrMin = 0
    print("Enter desired start year:")
    while yrMin not in yrList :               # while loop to ensure valid input
        try :
            yrMin = int(input('> '))
        except :
            print("Please enter a valid year")

    # filter according to specified year
    year_filter = df['year'] >= yrMin                                             # setting filter variable
    df = df.loc[year_filter, ['last_name', 'first_name', 'year', 'sex', 'veteran']] # applying filter and selecting relevent columns

    ###for debugging###
    #print(df.veteran.unique())
    #print(df[[ 'last_name' , 'first_name' , 'year' , 'veteran' , 'sex' ]].head(30))
    #print(df.sex.unique())
    print(f"\nResulting number of rows:  {len(df)}")
    #print(df.dtypes)
    #rint(df.head())

    totalVets(df)
    femaleVets(df)

    input()
    print()
    print(df.groupby(['year' , 'veteran']).size())
    sns.countplot(x='year', hue='veteran', data=df)
    plt.savefig('/home/student/static/countPlot2.png')

if __name__ == '__main__' :
    main()